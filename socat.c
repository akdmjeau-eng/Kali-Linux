#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <errno.h>

int main() {
    int sock;
    struct sockaddr_in moto_addr;
    moto_addr.sin_family = AF_INET;
    moto_addr.sin_port = htons(5555);
    inet_pton(AF_INET, "192.168.100.1", &moto_addr.sin_addr);

    printf("[*] Nexus Bridge: Esperando al Moto E13 en 192.168.100.1:5555...\n");

    while (1) {
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (connect(sock, (struct sockaddr *)&moto_addr, sizeof(moto_addr)) == 0) {
            printf("\n[+] ¡CONEXIÓN ESTABLECIDA! Puerto 5555 abierto.\n");
            // Aquí puedes lanzar tu exploit o redirigir el tráfico
            close(sock);
            break; 
        } else {
            // Error silencioso para no llenar la pantalla como socat
            printf("[-] Intentando...\r");
            fflush(stdout);
            close(sock);
            usleep(800000); // Esperar 0.8s para no saturar el Moto E13
        }
    }
    return 0;
}
