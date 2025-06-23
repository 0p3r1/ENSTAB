#include <stdio.h>
#include <stdlib.h>

int average_int_array(int array[], size_t size);
int parse_args_v2(int argc, char* argv[], int** args_array_ptr);

int main(int argc, char* argv[]){
	int* args_array;
       	int nb_read = parse_args_v2(argc, argv, &args_array);
	// passer le tableau à average_int_array
	int res = average_int_array(args_array, nb_read);
	printf("La moyenne est: %d\n", res);	
	// on libère la mémoire (inutile ici car le programme
	// termine, mais y penser quand on a un "vrai" programme
	free(args_array);
	return 0;
}

int parse_args_v2(int argc, char* argv[], int** args_array_ptr){
	if (argc <= 1){
		printf("Il faut des entiers en argument\n");
		// première solution renvoyer l'entier 0
		// et DOCUMENTER ce comportement
		// return 0;
		// ou seconde solution, arrêter le programme
		// et DOCUMENTER le sens du code d'erreur
		exit(1);
	}
 	// allouer de la mémoire sur le tas pour argc-1 entiers
	// dans le cadre de l'exercice on ne s'embête pas à traiter
	// la possibilité d'allouer exactement la bonne taille
	
	*args_array_ptr = malloc((argc - 1) * sizeof(int));

	int nb_read = 0;
	char* last_read_char;
	for(int i=1; i<argc; i++){
		// convertir argv[i] en entier
		// strtol
		
		// vérifier qu'on lit bien un entier
		int arg = strtol(argv[i], &last_read_char, 10);
		
		// après cet appel, last_read_char pointera vers
		// le premier caractère non numérique de argv[i]
		// => si ce n'est pas \0, on met à la poubelle
		// argv[i]
		// on imagine qu'on a une gestion d'erreur
		// par exemple on refuse les entiers > 100
		if (*last_read_char == '\0' && arg <= 100){
			// ATTENTION à ne pas utiliser i mais
			// nb_read pour ne pas "sauter" de cases
			// dans le tableau de résultats
			(*args_array_ptr)[nb_read] = arg;
			nb_read++;
		}
	}
	return nb_read;
}

//int average_int_array(int *array, size_t size){ //équivalent
int average_int_array(int array[], size_t size){
	int sum = 0;
	for (int i=0; i<size; i++){
		sum += array[i];
	}
	return sum/size;
}

