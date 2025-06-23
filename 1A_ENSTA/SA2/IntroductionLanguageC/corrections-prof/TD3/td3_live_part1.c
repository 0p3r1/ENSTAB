#include <stdio.h>
// Sécurité supplémentaire
#define ARR_LEN 4

int average_int(int, int);
int average_int2(int, int);
double average_double(double ,double);
int average_int_array(int array[], size_t size);

int main(void){
	// sécurité supplémentaire, si on spécifie la taille
	// en dur et qu'on met moins de valeurs => le tableau
	// est alloué et les cases non initialisées sont mises
	// à 0 => au moins on évite les dépassements mémoire !
	// Si on demande à initialiser plus de valeurs => warning
	// à la compilation !
	
	int arr[ARR_LEN]={4, 12, 3, 12}; 
	int res = average_int(5, 12);
	printf("%d\n", res);
	int res2 = average_int2(5, 12);
	printf("%d\n", res2);
	double resd = average_double(5, 12);
	printf("%lf\n", resd);
	int arr_mean = average_int_array(arr, ARR_LEN);
	printf("%d\n", arr_mean);
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

int average_int2(int a, int b){
	int arr[]={a, b};
	return average_int_array(arr, 2);
}

int average_int(int a, int b){
	return (a + b)/2;
}

double average_double(double a, double b){
	return (a + b)/2;
}


