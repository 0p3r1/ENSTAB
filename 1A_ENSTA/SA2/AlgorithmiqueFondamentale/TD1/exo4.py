import numpy as np
import exo1
import exo2


def fusion(tab1, tab2, d1, d2, taille):
    """
    tab1    : le tableau d'entrée, on fusionnera les données entre tab1[d1:d1+taille] et tab1[d2:d2+taille]. Elles doivent avoir été préalablement triées.
    tab2    : le tableau de sortie contenant les données fusionnées.
    d1      : l'indice du premier bloc à fusionner
    d2      : l'indice du deuxième bloc à fusionner, on suppose d2>d1
    taille  : la taille des blocs à fusionner
    """

    bloc1 = exo2.tri_insertion(tab1[d1 : d1 + taille])
    bloc2 = exo2.tri_insertion(tab1[d2 : d2 + taille])

    i = 0
    j = 0
    k = d1
    while i < taille and j < taille:
        if bloc1[i] <= bloc2[j]:
            tab2[k] = bloc1[i]
            i += 1
        else:
            tab2[k] = bloc2[j]
            j += 1
        k += 1

    while i < taille:
        tab2[k] = bloc1[i]
        i += 1
        k += 1

    while j < taille:
        tab2[k] = bloc2[j]
        j += 1
        k += 1

    return tab2


if __name__ == "__main__":
    t1 = np.array((4, 2, 3, 1))
    t2 = np.zeros((len(t1)))

    fusion(t1, t2, 0, 1, 1)
    print(t2)  # [2 4 0 0]
    fusion(t1, t2, 2, 3, 1)
    print(t2)  # [2 4 1 3]
    t1, t2 = t2, t1
    fusion(t1, t2, 0, 2, 2)
    print(t2)  # [1 2 3 4]
