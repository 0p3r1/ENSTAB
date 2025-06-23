#include <stdio.h>
#define N 10

#define TRUE 1
#define FALSE 0

int main(int argc, char* argv[]){
    int a[N];
    int b[N];

    int c = 5;
    int *c_ptr;
    c_ptr = &c;
    *c_ptr = 42;
    printf("c vaut %d\n", c);
    // on remplit a avec des valeurs
    for (int i = 0; i < N; i++)
        a[i] = i * i;

    int *a_ptr;
    a_ptr = a;
    int *b_ptr;
    b_ptr = b;
    /*
    // on recopie a dans b
    for (int i = 0; i < N; i++){
        // b_ptr[i] = a_ptr[i] ; aucun interet
        *(b_ptr + i) = *(a_ptr +i); // pas beaucoup plus d'interet
        printf("b_ptr + i: %p\n", b_ptr +i );
    }
    */
    while(a_ptr - a < N)
        *b_ptr++ = *a_ptr++;

    // parcours simultané de a et b
    for (int i = 0; i < N; i++)
        printf("%d - a[%d] = %d - b[%d] = %d\n", i, i, *(a + i), i,  b[i]);

    a_ptr = a;
    b_ptr = b;
    // avec la ligne suivante on peut forcer une erreur dans la
    // comparaison
    // a[0] = 42;
    int copy_OK = TRUE;
    while (a_ptr - a < N){
        if (*a_ptr++ != *b_ptr++) {
            copy_OK = FALSE;
            break;
        }
    }
    if (copy_OK)
        printf("a et b sont identiques\n");
    else
        printf("a et b sont differents\n");
    return 0;
}
