#include <stdio.h>

int main() {
    int n, i;

    // Asking for the number of elements in the array
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int array[n];

    // Reading the elements of the array
    printf("Enter the elements of the array:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // Replacing each element with its square
    for(i = 0; i < n; i++) {
        array[i] = array[i] * array[i];
    }

    // Printing the updated array
    printf("The array after replacing elements with their squares:\n");
    for(i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}
