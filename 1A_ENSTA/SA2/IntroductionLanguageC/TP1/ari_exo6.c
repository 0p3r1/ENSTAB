#include <stdio.h>

int main(void)
{
    int z = 2 >= 3 && 2;
    int x = 1 == 3 || 2;
    int y = x == z;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}