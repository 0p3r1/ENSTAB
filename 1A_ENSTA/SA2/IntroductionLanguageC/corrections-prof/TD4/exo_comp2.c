#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _student
{
    // le contenu de la structure
    char *name;
    int age;

    // où trouver la suite
    struct _student* next;
} student_t;

int append_many_students(char* names[], int ages[], int nb_to_add,
        student_t** list);

int append_student(char*,  int, student_t**);
void print_list(student_t *student_list);
int delete_student(char*, int, student_t**);

int main(int argc, char* argv[]){
    char *names[] = {"Foo", "Bar", "Baz"};
    int ages[] = {42, 45, 49};

    student_t* student_list = NULL;;
    
    printf("On rajoute Toto\n");
    append_student("Toto", 42, &student_list);
    print_list(student_list);
    printf("On rajoute tous les autres\n");
    append_many_students(names, ages, 3, &student_list);
    print_list(student_list);
    printf("On supprime Bar et Toto\n");
    delete_student("Bar", 3, &student_list);
    delete_student("Toto", 4, &student_list);
    // pour tester que ça ne plante pas
    delete_student("Plop", 4, &student_list);
    print_list(student_list);

    return 0;
}

int delete_student(char* name, int name_length, student_t** list_ptr){
    student_t **pp = list_ptr;
    student_t *to_delete;
    
    while(*pp){
        if(strncmp((*pp)->name, name, name_length) == 0 && 
           strlen((*pp)->name) == name_length){
            
            to_delete = *pp;
            *pp = (*pp)->next;
            free(to_delete);
            return 1;
        }
        pp = &((*pp)->next);
    }
    return 0;
}


void print_list(student_t* student_list){
    student_t* current_student_ptr;
    current_student_ptr = student_list;
    while(current_student_ptr){ // idem current_student_ptr != NULL
        printf("%s %d\n", current_student_ptr->name, current_student_ptr->age);
        current_student_ptr = current_student_ptr->next;
    }
}

int append_many_students(char* name[], int age[], int nb_to_add,
        student_t** list){
    // pas forcément la manière la plus efficace de faire car
    // append_student va à chaque fois chercher la fin de la liste
    // pour ajouter un élément

    int nb_done = 0;
    for (int i = 0; i < nb_to_add; i++){
        nb_done += append_student(name[i], age[i], list);
    }
    return nb_done;
}

int append_student(char* new_name, int new_age, student_t** list_ptr){
    student_t **pp = list_ptr;
    student_t *new;
    if (new_age < 0 || strlen(new_name) == 0){
        return 0;
    }

    //on va chercher la fin de la liste
    while(*pp){
	pp = &((*pp)->next);
    }
    new = malloc(sizeof(student_t));
    new->name = new_name;
    new->age = new_age;
    new->next = NULL;
    //on l'accroche à la liste
    *pp = new;
    return 1;
}
