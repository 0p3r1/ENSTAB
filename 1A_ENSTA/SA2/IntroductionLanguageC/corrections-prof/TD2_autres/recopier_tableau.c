#include <stdio.h>
#define N 10

#define TRUE 1
#define FALSE 0

int main(int argc, char* argv[]){
    int a[N];
    int b[N];

    // on remplit a avec des valeurs
    for (int i = 0; i < N; i++)
        a[i] = i * i;

    // on recopie a dans b
    for (int i = 0; i < N; i++)
        b[i] = a[i] ;

    // parcours simultané de a et b
    for (int i = 0; i < N; i++)
        printf("%d - a[%d] = %d - b[%d] = %d\n", i, i, a[i], i,  b[i]);

    a[0] = 42;
    int i = 0;
    int copy_OK = TRUE;
    while (i < N){
        if (a[i] != b[i]){
            copy_OK = FALSE;
            break;
        }
        i++;
    }
    if (copy_OK)
        printf("a et b sont identiques\n");
    else
        printf("a et b sont differents\n");
    // attention cela ne marche que si le tableau "a" est une variable locale !
    int n = sizeof(a)/sizeof(a[0]);
    printf("Raw array size ->  %ld, Size of int = %ld, Length of array = %d\n", sizeof(a), sizeof(a[0]), n);
    return 0;
}
