#include <stdio.h>

int main(void)
{
    int x = 3 > 2 > 1;
    int y = x++ + 1;
    int z = x || !y;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}