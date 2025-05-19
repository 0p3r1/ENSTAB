# TD1

## Types de données et affichage

1. **Rappeler les types de base du langage C.**

| Type     | Signification                | Exemples de valeur                            |
| -------- | ---------------------------- | --------------------------------------------- |
| `char`   | Caractère unique             | `'a' 'A' 'z' 'Z' '\n'`<br>Varie de –128 à 127 |
| `int`    | Nombre entier                | `0 1 -1 4589 32000`<br>`-231 à 231 +1`        |
| `float`  | Nombre réel simple           | `0.0 1.0 3.14 5.32 -1.23`                     |
| `double` | Nombre réel double précision | `0.0 1.0E–10 1.0 -1.34567896`                 |

2. **Rechercher dans la documentation de `printf` comment afficher le contenu de variables de ces types.**

| Type     | Spécificateur `printf` | Exemple de code              |
| -------- | ---------------------- | ---------------------------- |
| `char`   | `%c`                   | `printf("%c", maLettre);`    |
| `int`    | `%d` ou `%i`           | `printf("%d", monEntier);`   |
| `float`  | `%f`                   | `printf("%f", monFlottant);` |
| `double` | `%lf`                  | `printf("%lf", monDouble);`  |

3. **Comment représente-t-on un booléen ?**

En C, les booléens ne sont pas présents dans le langage d'origine (C89), mais on peut les utiliser via la bibliothèque standard à partir de C99 :

```c
#include <stdbool.h>
bool monBooleen = true;  // ou false
printf("%s", monBooleen ? "true" : "false");
```

> Sans `<stdbool.h>`, on peut utiliser un `int` avec `0` pour faux et tout autre entier pour vrai.

## Premier programme (normalement déjà fait en fin de cours 1)

```c
#include <stdio.h>

int main(int argc, char* argv[]){
        printf("Hello World !\n");
        return 0;
}
```

```sh
➜  TP1 git:(main) ✗ gcc -o hello hello.c
➜  TP1 git:(main) ✗ ./hello
Hello World !
```

## Programme qui affiche quelque chose

1. **Modifiez le code précédent pour lui faire afficher un texte prédéfini ("Je suis le deuxième programme").**

```c
#include <stdio.h>

int main(int argc, char* argv[]){
        printf("Je suis le deuxième programme\n");
        return 0;
}
```

```sh
➜  TP1 git:(main) ✗ gcc -o exo1 exo1.c
➜  TP1 git:(main) ✗ ./exo1
Je suis le deuxième programme
```

2. **Rejouer la procédure consistant à sauver le programme (sous le nom exo2.c), le compiler, l’exécuter, le tout en vérifiant l’absence d’erreur.**

```sh
➜  TP1 git:(main) ✗ gcc -o exo2 exo2.c
➜  TP1 git:(main) ✗ ./exo2
Je suis le deuxième programme
```

3. **Modifier le code précédent (exo3) pour définir trois variables a, b, et c correspondant à des entiers. On veut que le programme affiche le texte "<valeur de a> divisé par <valeur de b> vaut <valeur du résultat>" et passe à la ligne, avec résultat qui correspond à la division de a par b stockée dans c. Testez avec a=10 et b=3.**

```c
#include <stdio.h>

int main(int argc, char* argv[]) {
    int a = 10;
    int b = 3;
    int c = a / b;

    printf("%d divisé par %d vaut %d\n", a, b, c);
    return 0;
}
```

```sh
➜  TP1 git:(main) ✗ gcc -o exo3 exo3.c
➜  TP1 git:(main) ✗ ./exo3
10 divisé par 3 vaut 3
```

4. **Changer les types des variables et ajustez le code pour permettre un résultat exact (exo4).**

```c
#include <stdio.h>

int main(int argc, char* argv[]) {
    float a = 10.0;
    float b = 3.0;
    float c = a / b;

    printf("%.1f divisé par %.1f vaut %.2f\n", a, b, c);
    return 0;
}
```

```sh
➜  TP1 git:(main) ✗ gcc -o exo4 exo4.c
➜  TP1 git:(main) ✗ ./exo4
10.0 divisé par 3.0 vaut 3.33
```

## Arithmétique et opérateurs

**Calculez à la main le résultat de chacune des expressions suivantes, puis écrivez un programme qui affiche le résultat pour contrôler vos prédictions.**

1. `4−3*2−1`

> À la main : 3\*2 = 6 et 4-6-1 = -3

```c
#include <stdio.h>

int main(void) {
    int res = 4 - 3 * 2 - 1;
    printf("Résultat : %d\n", res);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo1 ari_exo1.c
➜  TP1 git:(main) ✗ ./ari_exo1
Résultat : -3
```

2. `2+3*6+7*2*−2/4`

> À la main : 3\*6 = 18 ; 7\*2\*−2 = -28 ; -28/4 = -7 ; 2 + 18 -7 = 13

```c
#include <stdio.h>

int main(void) {
    int res = 2+3*6+7*2*−2/4;
    printf("Résultat : %d\n", res);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo2 ari_exo2.c
➜  TP1 git:(main) ✗ ./ari_exo2
Résultat : 13
```

3. `8/4+2*10%5+3+2/1`

> À la main : 8/4 = 2 ; 2\*10%5 = 0 ; 2 + 0 + 5 = 7

```c
#include <stdio.h>

int main(void) {
    int res = 8/4+2*10%5+3+2/1;
    printf("Résultat : %d\n", res);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo3 ari_exo3.c
➜  TP1 git:(main) ✗ ./ari_exo3
Résultat : 7
```

4. `z = 10 −2; y = 4 * 2 ; x = z < y ++;`

> À la main : z = 8 ; y = 8, mais y++ => donc y = 9 ; x = 0

```c
#include <stdio.h>

int main(void) {
    int z = 10 - 2;
    int y = 4 * 2;
    int x = z < y++;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo4 ari_exo4.c
➜  TP1 git:(main) ✗ ./ari_exo4
x = 0, y = 9, z = 8
```

5. `x = 3 > 2 > 1 ; y = x ++ + 1 ; z = x | | ! y ;`

> À la main : x = 1 ; y = 1 ; z = 1

```c
#include <stdio.h>

int main(void) {
    int x = 3 > 2 > 1;
    int y = x++ + 1;
    int z = x || !y;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo5 ari_exo5.c
➜  TP1 git:(main) ✗ ./ari_exo5
x = 1, y = 1, z = 1
```

6. `z = 2 >= 3 && 2 ; x = 1 == 3 | | 2 ; y = x == z ;`

> À la main : z = 0 ; x = 1 ; y = 0

```c
#include <stdio.h>

int main(void) {
    int z = 2 >= 3 && 2;
    int x = 1 == 3 || 2;
    int y = x == z;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o ari_exo6 ari_exo6.c
ari_exo6.c:5:20: warning: use of logical '&&' with constant operand [-Wconstant-logical-operand]
    int z = 2 >= 3 && 2;
                   ^  ~
ari_exo6.c:5:20: note: use '&' for a bitwise operation
    int z = 2 >= 3 && 2;
                   ^~
                   &
ari_exo6.c:5:20: note: remove constant to silence this warning
    int z = 2 >= 3 && 2;
                  ~^~~~
ari_exo6.c:6:20: warning: use of logical '||' with constant operand [-Wconstant-logical-operand]
    int x = 1 == 3 || 2;
                   ^  ~
ari_exo6.c:6:20: note: use '|' for a bitwise operation
    int x = 1 == 3 || 2;
                   ^~
                   |
2 warnings generated.
```

```sh
➜  TP1 git:(main) ✗ ./ari_exo6
x = 1, y = 0, z = 0
```

## Structures conditionnelles

**On a la propriété suivante : trois nombre positifs sont les longueurs des cotés d’un triangle si et seulement si aucun de ces trois nombres n’est supérieur à la somme des deux autres. On suppose que a, b et c sont trois nombres ; écrire un programme qui affichera "<valeur de a>, <valeur de b>, <valeur de c> est bien un triangle" ou "<valeur de a>, <valeur de b>, <valeur de c> ne peut pas être un triangle" suivant les valeurs de a, b, c que vous choisirez avant la compilation.**

```c
#include <stdio.h>

int main(void) {
    int a = 3;
    int b = 4;
    int c = 5;

    if (a + b > c && a + c > b && b + c > a) {
        printf("%d, %d, %d est bien un triangle\n", a, b, c);
    } else {
        printf("%d, %d, %d ne peut pas être un triangle\n", a, b, c);
    }

    return 0;
}
```

```sh
➜  TP1 git:(main) gcc -o struct_condi struct_condi.c
➜  TP1 git:(main) ✗ ./struct_condi
3, 4, 5 est bien un triangle
```
