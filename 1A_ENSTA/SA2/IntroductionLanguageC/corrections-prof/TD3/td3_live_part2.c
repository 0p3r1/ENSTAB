#include <stdio.h>
#include <stdlib.h>

int average_int_array(int array[], size_t size);

int main(int argc, char* argv[]){
	if (argc <= 1){
		printf("Il faut des entiers en argument\n");
		return 1;
	}
	int array[argc - 1];
	for(int i=1; i<argc; i++){
		// convertir argv[i] en entier
		// strtol
		int arg = strtol(argv[i], NULL, 10);
		// remplir le tableau
		array[i - 1] = arg;
	}
	// passer le tableau à average_int_array
	int res = average_int_array(array, argc-1);
	printf("La moyenne est: %d\n", res);	
	return 0;
}

//int average_int_array(int *array, size_t size){ //équivalent
int average_int_array(int array[], size_t size){
	int sum = 0;
	for (int i=0; i<size; i++){
		sum += array[i];
	}
	return sum/size;
}

