# Arch CPU

Programa en Python para detectar la arquitectura de la CPU (ARM o x86).

## Descripción

`arch_cpu.py` es un pequeño script que identifica si el procesador de la máquina
donde se ejecuta es de arquitectura **ARM** o **x86**. Utiliza el módulo estándar
`platform` para obtener el nombre del hardware y el ancho de bits del ejecutable
de Python, clasificando el resultado en una categoría clara.

Incluye soporte para **Apple Silicon** (que reporta `arm64` / `aarch64`).

- **Autor:** Dr. Aldo Gonzalez Vazquez
- **Licencia:** MIT License

## Modo de uso

Ejecución directa desde la terminal:

```bash
python3 arch_cpu.py
```

Salida de ejemplo:

```
Arquitectura ARM detectada: 64bit
```

```
Arquitectura x86 detectada: 64bit
```

### Uso como módulo

También se puede importar la función de detección:

```python
import arch_cpu

print(arch_cpu.detectar_arquitectura("x86_64"))  # -> "x86"
print(arch_cpu.detectar_arquitectura("arm64"))   # -> "ARM"
print(arch_cpu.detectar_arquitectura("ppc"))     # -> None
```

## Estructura de la lógica

```
main()
│
├─ Obtiene `bits`   → platform.architecture()[0]  (64bit / 32bit)
├─ Obtiene `machine` → platform.machine().lower() (aarch64, x86_64, ...)
│
└─ detectar_arquitectura(machine)
   │
   ├─ Si machine ∈ {arm, armv6l, armv7l, armv8l, aarch64, arm64}  → "ARM"
   ├─ Si machine ∈ {x86, x86_64, amd64, i386, i486, i586, i686} → "x86"
   └─ En caso contrario                                           → None
        │
        └─ main imprime "Arquitectura desconocida" si es None
           o "Arquitectura {ARM/x86} detectada" en caso contrario
```

### Diagrama de flujo

```
[Inicio]
   |
   v
Obtener bits (ancho de bits de Python)
   |
   v
Obtener machine (nombre del hardware, en minúsculas)
   |
   v
¿ machine pertenece al conjunto ARM ?
   |                                    |
   Si                                   No
   |                                    |
   v                                    v
"ARM"                                  ¿ machine pertenece al conjunto x86 ?
                                        |                                    |
                                        Si                                   No
                                        |                                    |
                                        v                                    v
                                      "x86"                                 None
                                                                              |
                                                                              v
                                                                        "Desconocida"
```

### Conjuntos de detección

**ARM:** `arm`, `armv6l`, `armv7l`, `armv8l`, `aarch64`, `arm64`

**x86:** `x86`, `x86_64`, `amd64`, `i386`, `i486`, `i586`, `i686`

> Nota: Los valores se comparan con conjuntos exactos (no por substring) para
> evitar falsas coincidencias.
