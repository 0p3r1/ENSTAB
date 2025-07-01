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

student_t* create_list(void);
void create_list2(student_t*);
void create_list3(student_t**);
student_t create_list4(void);

int append_many_students(char* names[], int ages[], int nb_to_add,
        student_t* list);
int append_student(char*,  int, student_t*);
void print_list(student_t *student_list);
void print_list2(student_t student_list);
int count_and_get_last(student_t *list, student_t **last_ptr);
int insert(char* name, int age, int pos, student_t* list);

int main(int argc, char* argv[]){
    student_t* current_student_ptr;
    char *names[] = {"Foo", "Bar", "Baz"};
    int ages[] = {42, 45, 49};

    student_t* student_list;
    //student_list = create_list();

    // OU encore (vraiment compliqué)
    // create_list3(&student_list);

    // OU (plus courant)
    // student_t student_list_pas_ptr;
    // create_list2(&student_list_pas_ptr);

    // OU
    student_t student_list_pas_ptr;
    student_list_pas_ptr = create_list4();

    student_list = &student_list_pas_ptr; // pour ne pas casser la suite du code


    // on peut ne pas récupérer la valeur de retour
    // int append_ok;
    // append_ok = append_student("Toto", 42, student_list);
    //exemple avec un string literal
    
    append_student("Toto", 42, student_list);
    append_many_students(names, ages, 3, student_list);
    print_list(student_list);

    // exemple avec une chaîne qui n'est pas un string literal
    char* new_name = malloc(sizeof(char)*5);
    strncpy(new_name, "Tatu", 5);
    append_student(new_name, 42, student_list);

    print_list(student_list);
    // on se place sur l'étudiant fantôme
    current_student_ptr = student_list;

    // on cherche l'étudiant nommé "Bar"
    // NE PAS FAIRE CA !!! UTILISER STRCMP !!!
    // while(current_student_ptr->next != NULL && current_student_ptr->next->name != "Bar"){
    // ça ça marche:
    // while(current_student_ptr->next != NULL && strncmp(current_student_ptr->next->name, "Bar", 3) != 0) {
    // version courte
    student_t *to_delete;
    while(current_student_ptr->next  && strncmp(current_student_ptr->next->name, "Bar", 3)) {
        current_student_ptr = current_student_ptr->next;
    }
    to_delete = current_student_ptr->next;
    current_student_ptr->next = to_delete->next;
    free(to_delete);

    print_list2(student_list_pas_ptr);

    student_t *last_ptr;
    int list_len = count_and_get_last(student_list, &last_ptr);
    printf("Il y a %d étudiants, le dernier est %s\n", list_len, last_ptr->name);

    int check_insert;
    check_insert = insert("Marcel", 28, 3, student_list);
    if(!check_insert){
	    printf("Ajout impossible\n");
    }
    check_insert = insert("Jean-Marcel", 28, 50, student_list);
    if(!check_insert){
	    printf("Ajout impossible\n");
    }
    print_list(student_list);
   return 0;
}
void print_list(student_t* student_list){
    student_t* current_student_ptr;
    // exemple de parcours de la liste (à mettre dans une fonction !)
    current_student_ptr = student_list->next;
    while(current_student_ptr){ // idem current_student_ptr != NULL
        printf("%s %d\n", current_student_ptr->name, current_student_ptr->age);
        current_student_ptr = current_student_ptr->next;
    }
}

void print_list2(student_t student_list){
    student_t* current_student_ptr;
    // exemple de parcours de la liste (à mettre dans une fonction !)
    current_student_ptr = student_list.next;
    while(current_student_ptr){ // idem current_student_ptr != NULL
        printf("%s %d\n", current_student_ptr->name, current_student_ptr->age);
        current_student_ptr = current_student_ptr->next;
    }
}


student_t* create_list(void){
    student_t* ghost;
    ghost = malloc(sizeof(student_t));
   // on peut initialiser, ou pas, le point d'entrée comme un élément valide
    // ici "ou pas", c'est plus simple à gérer car la liste contient toujours
    // au moins un élément fantôme qu'on prendra garde à "sauter" lors du parcours.
    ghost->name = NULL;
    ghost->age = -1;
    ghost->next = NULL;
    return ghost;
}

void create_list3(student_t** ghost){
    *ghost = malloc(sizeof(student_t));
    (*ghost)->name = NULL;
    (*ghost)->age = -1;
    (*ghost)->next = NULL;
}

void create_list2(student_t* ghost){
   // on peut initialiser, ou pas, le point d'entrée comme un élément valide
    // ici "ou pas", c'est plus simple à gérer car la liste contient toujours
    // au moins un élément fantôme qu'on prendra garde à "sauter" lors du parcours.
    ghost->name = NULL;
    ghost->age = -1;
    ghost->next = NULL;
    return;
}

student_t create_list4(void){
    /*
    student_t ghost;
    ghost.name = NULL;
    ghost.age = -1;
    ghost.next = NULL;
    return ghost;
    */
    // voire carrément (commenter tout le code au dessus)
    return (student_t){NULL, -1, NULL};
}

int append_many_students(char* name[], int age[], int nb_to_add,
        student_t* list){
    // pas forcément la manière la plus efficace de faire car
    // append_student va à chaque fois chercher la fin de la liste
    // pour ajouter un élément

    int nb_done = 0;
    for (int i = 0; i < nb_to_add; i++){
        nb_done += append_student(name[i], age[i], list);
    }
    return nb_done;
}

int count_and_get_last(student_t *list, student_t **last_ptr_ptr){
    int cpt = 0;
    while (list->next){
        cpt += 1;
        list = list->next;
    }
    *last_ptr_ptr = list; //list pointe maintenant sur le dernier élément
    return cpt;
}

int insert(char* name, int age, int pos, student_t* list){
    student_t* new;
    while(list->next && pos){ //list->next != NULL && pos != 0
        list = list->next;
        pos--;
    }


    if (pos){ // i.e pos != 0 on n'a pas atteint l'élément demandé, la liste est trop courte
        return 0;
    }



    new = malloc(sizeof(student_t));
    new->name = name;
    new->age = age;

    //le suivant du nouveau est le suivant du courant
    new->next = list->next;

    //on l'accroche à la liste
    list->next = new;
    return 1;
}

int append_student(char* new_name, int new_age, student_t* list){
    student_t *new;
    if (new_age < 0 || strlen(new_name) == 0){
        return 0;
    }

    //on va chercher la fin de la liste
    while(list->next){
        list = list->next;
    }
    //ici list pointe vers le dernier étudiant

    // ca va planter si name pointe vers un string literal
    // name[2] = 'L';
    new = malloc(sizeof(student_t));

    // attention ceci n'est PAS une copie de chaînes de caractères mais
    // une affectation de pointeurs
    new->name = new_name;

    // ici c'est bien une copie d'entiers
    new->age = new_age;

    //le nouveau est le dernier
    new->next = NULL;

    //on l'accroche à la liste
    list->next = new;
    return 1;
}

// exercices:
    // q0: supprimer l'étudiant nommé "Bar" en gardant une liste cohérente, le vérifier en affichant la liste
    // Pour la suite partir éventuellement sur un nouveau fichier dans lequel on fera des copier/coller judicieux
    // q1: écrire une fonction qui renvoie une liste contenant uniquement un étudiant fantôme
    // q2: écrire une fonction qui rajoute un nom/age en fin d'une liste d'élèves passée en argument, la fonction renvoie 1 si l'ajout se
    // passe bien, 0 si l'age ou le nom sont invalides (nom de 0 lettre, age négatif, etc).
    // q2bis: écrire une fonction qui rajoute plusieurs noms/ages en fin de liste en appelant q2, la fonction renvoie le nombre
    // d'élèves qui ont été ajoutés
    // q2ter: bien évidemment tester si ça marche avec les étudiants Foo, Bar et Baz
    // q3: faire une fonction qui affiche le contenu de la liste
    // q4: écrire une fonction qui prend une liste en paramètre, renvoie son nombre d'éléments et modifie une variable
    // passée en paramètre pour qu'elle pointe vers le dernier élément
    // q5: écrire une fonction qui prend en paramètre le nom d'un étudiant, son age, une position dans la liste et une liste d'étudiants
    //  et ajoute cet étudiant dans la liste à la position demandée
