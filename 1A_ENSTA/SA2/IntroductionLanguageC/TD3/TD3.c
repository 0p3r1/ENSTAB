#include <stdlib.h>
#include <stdio.h>

double average_int(int a, int b) {
    return (a + b) / 2.0;
}

double average_double(double a, double b) {
    return (a + b) / 2.0;
}

double average_int_array(int array[], int size) {
    double sum = 0.0;
    for (int i = 0; i < size; ++i) {
        sum += array[i];
    }
    return sum / size;
}

int main(void) {
    printf("average_int(1,2) : %f\n", average_int(1,2));
    printf("average_double(15.0,30.0) : %f\n", average_double(15.0,30.0));

    int arr[] = {1, 8, 3, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("average_int_array({1, 8, 3, 5}, %d) : %f\n", size, average_int_array(arr, size));

    return 0;
}