#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 42

int main () {
   time_t t;
   int rand_array[ARRAY_SIZE];
   
   /* Intializes random number generator */
   srand((unsigned) time(&t));

   for(int i = 0 ; i < ARRAY_SIZE ; i++ ) {
      rand_array[i] = rand() % 50;
      printf("%d ", rand_array[i]);
   }
   printf("\n");
   
   return(0);
}