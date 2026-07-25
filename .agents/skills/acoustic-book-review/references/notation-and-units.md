# Notación y unidades recomendadas

Adaptar estas convenciones al preámbulo existente. No cambiar símbolos consolidados sin revisar todas sus apariciones.

## Ondas y oscilaciones

| Magnitud | Símbolo sugerido | Unidad |
|---|---:|---:|
| tiempo | `t` | s |
| frecuencia | `f` | Hz |
| período | `T` | s |
| frecuencia angular | `\omega = 2\pi f` | rad/s |
| fase inicial | `\varphi` | rad |
| longitud de onda | `\lambda` | m |
| velocidad de propagación | `c` | m/s |
| desplazamiento de partícula | `\xi` | m |
| velocidad de partícula | `u` | m/s |

Una sinusoide debe identificar la magnitud representada. Preferir, por ejemplo:

```tex
p(t)=\hat p\sin(2\pi f t+\varphi)
```

en lugar de `x(t)` cuando se hable específicamente de presión acústica.

## Magnitudes acústicas

| Magnitud | Símbolo sugerido | Unidad |
|---|---:|---:|
| presión acústica instantánea | `p(t)` | Pa |
| presión eficaz | `p_\mathrm{rms}` | Pa |
| intensidad acústica | `I` o `\mathbf{I}` | W/m² |
| potencia acústica | `W` | W |
| densidad del medio | `\rho` | kg/m³ |
| impedancia característica | `Z_0=\rho c` | Pa·s/m |

No afirmar que la presión “determina” por sí sola la intensidad sin declarar el campo o la relación de impedancia aplicable.

## Niveles

En aire, para presión eficaz:

```tex
L_p = 20\log_{10}\!\left(\frac{p_\mathrm{rms}}{p_0}\right),
\qquad p_0=\SI{20}{\micro\pascal}.
```

Para intensidad y potencia:

```tex
L_I = 10\log_{10}\!\left(\frac{I}{I_0}\right),
\qquad
L_W = 10\log_{10}\!\left(\frac{W}{W_0}\right).
```

Reglas:

- El decibel expresa una relación logarítmica.
- Especificar la magnitud y la referencia al expresar un nivel absoluto.
- No usar `dB`, `dB SPL`, `dB HL`, `dB SL` y `dB(A)` como intercambiables.
- `dB HL` depende de frecuencia, transductor y referencia audiométrica; no convertirlo directamente desde `dB SPL` sin los datos de calibración correspondientes.
- La referencia de presión depende del medio y la convención; no usar automáticamente la referencia de aire en agua.
- Explicar por qué aparece 20 cuando la magnitud de energía es proporcional al cuadrado de una amplitud.

## Valores de una señal

Distinguir:

- valor instantáneo;
- amplitud de pico;
- valor pico a pico;
- valor medio;
- valor absoluto medio;
- valor eficaz o RMS.

Para una sinusoide de pico `\hat p` y media nula:

```tex
p_\mathrm{rms}=\frac{\hat p}{\sqrt{2}}.
```

## Percepción

Usar estas relaciones con cautela:

- mayor frecuencia suele asociarse con mayor pitch para tonos simples, pero no son sinónimos;
- mayor SPL suele aumentar la sonoridad, pero la sonoridad depende también de frecuencia, duración, ancho de banda y contexto;
- el timbre se relaciona con espectro y evolución temporal, pero no se reduce a una sola gráfica;
- “volumen” es un término cotidiano o de control de ganancia; no usarlo como nombre de una magnitud acústica.

## Escritura de unidades

- `K` para kelvin, sin `°`.
- `°C` para grados Celsius.
- Espacio entre valor y unidad mediante el mecanismo del proyecto, preferentemente `siunitx`.
- Símbolos de unidades sin plural y sin punto.
- Coma decimal en el texto en español, manteniendo compatibilidad con la configuración de LaTeX.
- Separar el símbolo de magnitud de la unidad: `p` no es “Pa”; se mide en Pa.
