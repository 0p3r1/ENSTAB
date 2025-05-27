#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 42

void triParComptage(int tab[]) {
   int borneSuperieure = 0;

   for (int i = 0; i < ARRAY_SIZE; i++) {
      if (tab[i] > borneSuperieure) {
         borneSuperieure = tab[i];
      }
   }

   int tabComptage[borneSuperieure + 1];
   for (int i = 0; i <= borneSuperieure; i++) {
      tabComptage[i] = 0;
   }

   for (int i = 0; i < ARRAY_SIZE; i++) {
      tabComptage[tab[i]]++;
   }

   int cpt = 0;
   for (int i = 0; i <= borneSuperieure; i++) {
      for (int j = 0; j < tabComptage[i]; j++) {
         tab[cpt] = i;
         cpt++;
      }
   }
}

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

   triParComptage(rand_array);

   for (int i = 0; i < ARRAY_SIZE; i++) {
      printf("%d ", rand_array[i]);
   }
   printf("\n");
   
   return(0);
}