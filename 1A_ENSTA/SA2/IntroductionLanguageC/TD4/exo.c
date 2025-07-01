#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _student
{
    char *name;
    int age;
    struct _student* next;
} student_t;

student_t* create_ghost_student_list() {
    student_t* ghost = (student_t*)malloc(sizeof(student_t));
    if (ghost == NULL) {
        perror("Erreur lors de l'allocation de l'étudiant fantôme");
        exit(EXIT_FAILURE);
    }
    ghost->name = NULL;
    ghost->age = -1;
    ghost->next = NULL;
    return ghost;
}

int add_student(student_t* student_list, const char* name, int age) {
    if (name == NULL || strlen(name) == 0 || age < 0) {
        return 0;  // Nom vide ou âge invalide
    }

    student_t* new_student = (student_t*)malloc(sizeof(student_t));
    if (new_student == NULL) {
        perror("Erreur lors de l'allocation de l'étudiant");
        exit(EXIT_FAILURE);
    }

    new_student->name = strdup(name); // Copier le nom
    new_student->age = age;
    new_student->next = NULL;

    // On parcourt la liste pour ajouter le nouvel étudiant à la fin
    student_t* current_student_ptr = student_list;
    while (current_student_ptr->next != NULL) {
        current_student_ptr = current_student_ptr->next;
    }
    
    // Ajouter le nouvel étudiant
    current_student_ptr->next = new_student;
    
    return 1;  // Ajout réussi
}

int add_multiple_students(student_t* student_list, char* names[], int* ages, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (add_student(student_list, names[i], ages[i])) {
            count++;
        }
    }
    return count;  // Nombre d'étudiants ajoutés
}

void print_student_list(student_t* student_list) {
    student_t* current_student_ptr = student_list->next; // Sauter l'étudiant fantôme
    while (current_student_ptr) {
        printf("%s %d\n", current_student_ptr->name, current_student_ptr->age);
        current_student_ptr = current_student_ptr->next;
    }
}

int main(int argc, char* argv[]){
    student_t* student_list = create_ghost_student_list();
    student_t* current_student_ptr;
    char *names[] = {"Foo", "Bar", "Baz"};
    int ages[] = {42, 45, 49};

    // Ajouter les étudiants Foo, Bar, Baz à la liste
    for (int i = 0; i < 3; i++) {
        add_student(student_list, names[i], ages[i]);
    }

    printf("Liste avant ajout de nouveaux étudiants:\n");
    print_student_list(student_list);

    // Ajouter plusieurs nouveaux étudiants
    char *new_names[] = {"Alice", "Bob", "Charlie"};
    int new_ages[] = {25, 30, 35};
    int added = add_multiple_students(student_list, new_names, new_ages, 3);

    printf("Nouveaux étudiants ajoutés: %d\n", added);
    printf("Liste après ajout de nouveaux étudiants:\n");
    print_student_list(student_list);

    return 0;
}
