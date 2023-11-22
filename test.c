#include <stdio.h>

extern char** environ;

int main() {
    printf("Content-Type: text/plain\n\nHello World!\n");

    printf("\nEnvironment:\n");
    for (int i = 0; environ[i] != NULL; ++i){
        printf("%s\n",environ[i]);
    }

    printf("\nInput:\n");
    char buffer[100];
    while(fgets(buffer, 100, stdin)) {
        printf("%s", buffer);
    }
    printf("\n");

    return 0;
}
