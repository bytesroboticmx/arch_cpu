//Programa para detectar la arquitectura de la CPU (ARM o x86).
//Autor: Dr. Aldo Gonzalez Vazquez
//Fecha: 29/09/2026
//Licencia: MIT License
import java.util.Set;

public class arch_cpu {

    private static String detectarArquitectura(String machine) {
        Set<String> arm = Set.of("arm", "armv6l", "armv7l", "armv8l", "aarch64", "arm64");
        Set<String> x86 = Set.of("x86", "x86_64", "amd64", "i386", "i486", "i586", "i686");

        if (arm.contains(machine)) {
            return "ARM";
        }
        if (x86.contains(machine)) {
            return "x86";
        }
        return null;
    }

    public static void main(String[] args) {
        String osArch = System.getProperty("os.arch").toLowerCase();
        String arch = detectarArquitectura(osArch);

        // En Java, "os.arch" es el ancho de bits de la JVM.
        String bits = System.getProperty("sun.arch.data.model");

        if (arch != null) {
            System.out.printf("Arquitectura %s detectada: %s%n", arch, bits);
        } else {
            System.out.printf("Arquitectura desconocida: %s, %s%n", osArch, bits);
        }
    }
}
