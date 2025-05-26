#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int a = 4;
    int b = 6;

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}