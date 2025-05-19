#include <stdio.h>

int main(void)
{
    int a = 3;
    int b = 4;
    int c = 5;

    if (a + b > c && a + c > b && b + c > a)
    {
        printf("%d, %d, %d est bien un triangle\n", a, b, c);
    }
    else
    {
        printf("%d, %d, %d ne peut pas être un triangle\n", a, b, c);
    }

    return 0;
}