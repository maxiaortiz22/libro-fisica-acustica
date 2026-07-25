#!/usr/bin/env python3
"""Heuristic checks for a LaTeX book repository.

This script does not parse TeX completely. It reports likely issues so they can be
reviewed by a human or by Codex before/after compilation.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "build",
    "out",
    "dist",
    "__pycache__",
}

LABEL_RE = re.compile(r"\\label\s*\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\s*\{([^}]+)\}")
CITE_RE = re.compile(r"\\(?:cite|parencite|textcite|autocite|footcite)\w*\s*(?:\[[^]]*\]\s*)*\{([^}]+)\}")
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}")
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
TODO_RE = re.compile(r"(?:TODO|FIXME|PENDIENTE|VERIFY|TODO\(verify\))", re.IGNORECASE)
ABSOLUTE_PATH_RE = re.compile(r"(?:[A-Za-z]:[\\/]|/(?:Users|home|mnt|tmp)/)")

GRAPHIC_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".svg", ".eps")
TEX_EXTENSIONS = ("", ".tex")


def iter_tex_files(root: Path):
    for path in root.rglob("*.tex"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        escaped = False
        kept = []
        for char in line:
            if char == "%" and not escaped:
                break
            kept.append(char)
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        lines.append("".join(kept))
    return "\n".join(lines)


def resolve_candidate(base: Path, raw: str, extensions: tuple[str, ...]) -> bool:
    raw = raw.strip()
    if not raw or "\\" in raw or "#" in raw:
        return True  # Dynamic TeX path; cannot validate reliably.
    candidate = (base / raw)
    if candidate.suffix:
        return candidate.exists()
    return any(candidate.with_suffix(ext).exists() if ext else candidate.exists() for ext in extensions)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="LaTeX project root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    tex_files = list(iter_tex_files(root))
    if not tex_files:
        print(f"ERROR: no .tex files found under {root}")
        return 2

    labels: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    refs: list[tuple[str, Path, int]] = []
    citations: Counter[str] = Counter()
    missing_graphics: list[tuple[str, Path, int]] = []
    missing_inputs: list[tuple[str, Path, int]] = []
    todos: list[tuple[Path, int, str]] = []
    absolute_paths: list[tuple[Path, int, str]] = []

    for path in tex_files:
        raw_text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, raw_line in enumerate(raw_text.splitlines(), 1):
            if TODO_RE.search(raw_line):
                todos.append((path, line_no, raw_line.strip()))
            if ABSOLUTE_PATH_RE.search(raw_line):
                absolute_paths.append((path, line_no, raw_line.strip()))

        text = strip_comments(raw_text)
        for line_no, line in enumerate(text.splitlines(), 1):
            for label in LABEL_RE.findall(line):
                labels[label].append((path, line_no))
            for ref in REF_RE.findall(line):
                refs.append((ref, path, line_no))
            for group in CITE_RE.findall(line):
                for key in group.split(","):
                    if key.strip():
                        citations[key.strip()] += 1
            for graphic in INCLUDEGRAPHICS_RE.findall(line):
                if not resolve_candidate(path.parent, graphic, GRAPHIC_EXTENSIONS):
                    missing_graphics.append((graphic, path, line_no))
            for item in INPUT_RE.findall(line):
                if not resolve_candidate(path.parent, item, TEX_EXTENSIONS):
                    missing_inputs.append((item, path, line_no))

    duplicate_labels = {key: locs for key, locs in labels.items() if len(locs) > 1}
    undefined_refs = [(key, path, line) for key, path, line in refs if key not in labels]

    def rel(path: Path) -> str:
        try:
            return str(path.relative_to(root))
        except ValueError:
            return str(path)

    print(f"Scanned {len(tex_files)} TeX files under {root}")
    print(f"Labels: {len(labels)} | References: {len(refs)} | Citation keys used: {len(citations)}")

    issues = 0

    if duplicate_labels:
        issues += len(duplicate_labels)
        print("\nDUPLICATE LABELS")
        for key, locations in sorted(duplicate_labels.items()):
            places = ", ".join(f"{rel(path)}:{line}" for path, line in locations)
            print(f"- {key}: {places}")

    if undefined_refs:
        issues += len(undefined_refs)
        print("\nPOSSIBLY UNDEFINED REFERENCES")
        for key, path, line in undefined_refs:
            print(f"- {rel(path)}:{line}: {key}")

    if missing_graphics:
        issues += len(missing_graphics)
        print("\nPOSSIBLY MISSING GRAPHICS")
        for item, path, line in missing_graphics:
            print(f"- {rel(path)}:{line}: {item}")

    if missing_inputs:
        issues += len(missing_inputs)
        print("\nPOSSIBLY MISSING INPUT/INCLUDE FILES")
        for item, path, line in missing_inputs:
            print(f"- {rel(path)}:{line}: {item}")

    if absolute_paths:
        issues += len(absolute_paths)
        print("\nABSOLUTE PATHS")
        for path, line, content in absolute_paths:
            print(f"- {rel(path)}:{line}: {content}")

    if todos:
        print("\nTODO / VERIFICATION MARKERS")
        for path, line, content in todos:
            print(f"- {rel(path)}:{line}: {content}")

    if not issues:
        print("\nNo heuristic structural issues found.")
    else:
        print(f"\nFound {issues} heuristic issue(s). Review before treating them as real TeX errors.")

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
