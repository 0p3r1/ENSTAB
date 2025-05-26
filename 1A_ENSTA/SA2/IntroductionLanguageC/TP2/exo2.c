#include <stdio.h>

int main(void)
{
    char texte[6] = "ENSTA";
    char texte_inverse[6];

    int len = 5;
    texte_inverse[len] = '\0';

    for (int i = 0; i < 5; i++)
    {
        texte_inverse[i] = texte[len - 1];
        len--;
    }

    printf("Le texte inversé de : '%s' est : '%s'\n", texte, texte_inverse);

    return 0;
}