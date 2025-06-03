#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int a = 4;
    int* pa = &a;

    printf("La valeur de a : %d\n", a);
    printf("L'adresse de a (pa) : %p\n", (void*)pa);

    for (int i = 1; i <= a; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
        system("sleep 1");
    }

    *pa = 5;

    printf("La nouvelle valeur de a après modification via pa : %d\n", a);

    return 0;
}
