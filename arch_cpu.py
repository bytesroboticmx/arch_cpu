#Programa para detectar la arquitectura de la CPU (ARM o x86).
#Autor: Dr. Aldo Gonzalez Vazquez
#Fecha: 01/09/2025
#Licencia: MIT License
import platform

def detectar_arquitectura(machine):
    arm = {'arm', 'armv6l', 'armv7l', 'armv8l', 'aarch64', 'arm64'}
    x86 = {'x86', 'x86_64', 'amd64', 'i386', 'i486', 'i586', 'i686'}

    if machine in arm:
        return "ARM"
    if machine in x86:
        return "x86"
    return None

def main():
    bits, _ = platform.architecture()
    machine = platform.machine().lower()
    arch = detectar_arquitectura(machine)

    if arch:
        print(f"Arquitectura {arch} detectada: {bits}")
    else:
        print(f"Arquitectura desconocida: {machine}, {bits}")

if __name__ == "__main__":
    main()
