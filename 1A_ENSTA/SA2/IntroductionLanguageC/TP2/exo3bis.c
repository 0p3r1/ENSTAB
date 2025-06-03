#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int a = 4;

    for (int i = 1; i <= a; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
        system("sleep 1");
    }

    return 0;
}