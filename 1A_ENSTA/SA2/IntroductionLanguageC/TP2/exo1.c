#include <stdio.h>

int main(void)
{
    int tableau[8] = {4, 7, -3, 10, 2, 5, 3, -1};

    int somme = 0;

    for (int i = 0; i < 8; i++)
    {
        somme += tableau[i];
    }

    printf("La somme des elements du tableau est : %d\n", somme);

    return 0;
}