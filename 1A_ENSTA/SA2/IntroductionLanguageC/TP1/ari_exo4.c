#include <stdio.h>

int main(void)
{
    int z = 10 - 2;
    int y = 4 * 2;
    int x = z < y++;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}