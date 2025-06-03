#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char tableau[] = {'u', 'n', ' ', 'p', 'o', 'i', 'n', 't', 'e', 'u', 'r', '\0'};

    printf("L'adresse de tableau : %p\n", (void*)tableau);
    printf("La chaîne de caractères : %s\n", tableau);

    char* p = tableau;
    while (*p != '\0') {
        p++;
    }
    printf("La taille de la chaîne (nombre de caractères avant '\\0') : %ld\n", p - tableau);

    tableau[8] = '\0';
    printf("Après avoir modifié à addr+8 : %s\n", tableau);

    char* ptr = &tableau[8];
    *ptr = 'e';
    
    printf("Texte après restauration : %s\n", tableau);

    return 0;
}
