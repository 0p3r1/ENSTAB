#include <stdio.h>
#include <stdlib.h>

int average_int_array(int array[], size_t size);
int* parse_args_v1(int argc, char* argv[]);

int main(int argc, char* argv[]){
	int* args_array = parse_args_v1(argc, argv);
	// passer le tableau à average_int_array
	int res = average_int_array(args_array, argc-1);
	printf("La moyenne est: %d\n", res);	
	// on libère la mémoire (inutile ici car le programme
	// termine, mais y penser quand on a un "vrai" programme
	free(args_array);
	return 0;
}

int* parse_args_v1(int argc, char* argv[]){
	int* array;
	if (argc <= 1){
		printf("Il faut des entiers en argument\n");
		// première solution renvoyer un pointeur nul
		// et DOCUMENTER ce comportement
		// return NULL;
		// ou seconde solution, arrêter le programme
		// et DOCUMENTER le sens du code d'erreur
		exit(1);
	}
 	//allouer de la mémoire sur le tas pour argc-1 entiers
	array = malloc((argc - 1) * sizeof(int));

	for(int i=1; i<argc; i++){
		// convertir argv[i] en entier
		// strtol
		int arg = strtol(argv[i], NULL, 10);
		// remplir le tableau
		array[i - 1] = arg;
	}
	return array;
}

//int average_int_array(int *array, size_t size){ //équivalent
int average_int_array(int array[], size_t size){
	int sum = 0;
	for (int i=0; i<size; i++){
		sum += array[i];
	}
	return sum/size;
}

