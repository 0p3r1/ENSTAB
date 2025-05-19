#include <stdio.h>

int main(int argc, char *argv[])
{
    float a = 10.0;
    float b = 3.0;
    float c = a / b;

    printf("%.1f divisé par %.1f vaut %.2f\n", a, b, c);
    return 0;
}