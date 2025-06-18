#include <stdio.h>
#include <stdint.h>
#define NB_CHAR 16
#define NB_INT 4
#define NB_DOUBLE 2

int main(void){
/* On a reçu les données suivantes via un système d'acquisition quelconque.
 * On sait que ces données sont codées comme suit:
 * 	- les NB_CHAR premiers octets codent chacun un char
 * 	- il y a ensuite NB_INT entiers codés chacun sur deux octets
 * 	- puis NB_DOUBLE double codés chacun sur huit octets
 *
 * => Extraire et afficher les données en utilisant des pointeurs et en jouant sur le transtypage
 * => Si ce n'est pas déjà fait, au lieu de parcourir les octets un à un, déclarer et initialiser
 * 	des pointeurs de char, int et double, pointant chacun vers la zone de mémoire appropriée.
 * => Pour finir déclarer une structure nommée intitulée sensor_data_t contenant les champs suivant:
 * 	- text, pour contenir les char reçus
 * 	- int_values, pour les entiers
 * 	- double_values, pour les double.
 *    Faire pointer cette structure sur data et utiliser les champs nommés pour afficher le 
 *      contenu.
 */

	uint8_t data[] = "\x44\x61\x74\x61\x20\x72\x65\x63\x65\x69\x76\x65\x64\x3a\x20\x20\t\x00\n\x00*\x00\x08\x00\x18-DT\xfb!\t@iW\x14\x8b\n\xbf\x05@";

    char* les_chars;
    uint16_t* les_entiers;
    double* les_doubles;

    les_chars = (char*) data;
    printf("%s\n", les_chars);

    les_entiers = (uint16_t*)(data + NB_CHAR);
    printf("Entiers: ");
    for (int i = 0; i < NB_INT; i++) {
        printf("%d ", les_entiers[i]);
    }
    printf("\n");

    les_doubles = (double*)(data + NB_CHAR + NB_INT * 2);
    printf("Doubles: ");
    for (int i = 0; i < NB_DOUBLE; i++) {
        printf("%lf ", les_doubles[i]);
    }
    printf("\n");

	return 0;
}