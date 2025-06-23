#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
    char src[] = "zorglubpouetpouet";
    char *dst;
    // la ligne suivante introduit exprès un bug 
    // *(src + 17) = 'a';  // bug exprès pour enlever le \0 dans src
    int src_len = strlen(src); 
    dst = (char *)malloc(sizeof(char) * (src_len + 1)); // +1 pour \0

    char  *dst_ptr = dst;
    char  *src_ptr = src;
    while(src_len--)
        *dst_ptr++ = *src_ptr++;

    *dst_ptr = '\0';
    printf("source: %s\n", src);
    printf("copie: %s\n", dst);
    return 0;
}
