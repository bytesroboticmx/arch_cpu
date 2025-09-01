#Programa para detectar la arquitectura de la CPU (ARM o x86).
#Autor: Dr. Aldo Gonzalez Vazquez
#Fecha: 01/09/2025
#Licencia: MIT License
import platform

def main():
    arch, _ = platform.architecture()
    machine = platform.machine().lower()

    if 'arm' in machine or 'aarch64' in machine:
        print(f"Arquitectura ARM detectada: {arch}")
    elif 'x86' in machine or 'amd64' in machine or 'i386' in machine:
        print(f"Arquitectura x86 detectada: {arch}")
    else:
        print(f"Arquitectura desconocida: {machine}, {arch}")

if __name__ == "__main__":
    main()
