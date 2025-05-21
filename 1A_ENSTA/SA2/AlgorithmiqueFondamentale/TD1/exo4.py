import numpy as np
import exo1


def fusion(tab1, tab2, d1, d2, taille):
    """
    tab1    : le tableau d'entrée, on fusionnera les données entre tab1[d1:d1+taille] et tab1[d2:d2+taille]. Elles doivent avoir été préalablement triées.
    tab2    : le tableau de sortie contenant les données fusionnées.
    d1      : l'indice du premier bloc à fusionner
    d2      : l'indice du deuxième bloc à fusionner, on suppose d2>d1
    taille  : la taille des blocs à fusionner
    """

    i = d1
    j = d2
    k = d1

    while i < d1 + taille and i < len(tab1) and j < d2 + taille and j < len(tab1):
        if tab1[i] <= tab1[j]:
            tab2[k] = tab1[i]
            i += 1
        else:
            tab2[k] = tab1[j]
            j += 1
        k += 1

    while i < d1 + taille and i < len(tab1):
        tab2[k] = tab1[i]
        i += 1
        k += 1

    while j < d2 + taille and j < len(tab1):
        tab2[k] = tab1[j]
        j += 1
        k += 1

    return tab2


def tri_fusion(tab):
    taille = len(tab)
    t2 = np.zeros_like(tab)

    taille_bloc = 1
    while taille_bloc < taille:
        for i in range(0, taille, 2 * taille_bloc):
            j = min(i + taille_bloc, taille)
            fusion(tab, t2, i, j, taille_bloc)
        tab, t2 = t2, tab
        taille_bloc *= 2

    return tab


if __name__ == "__main__":
    # t1 = np.array((4, 2, 3, 1))
    # t2 = np.zeros((len(t1)))

    # fusion(t1, t2, 0, 1, 1)
    # print(t2)  # [2 4 0 0]
    # fusion(t1, t2, 2, 3, 1)
    # print(t2)  # [2 4 1 3]
    # t1, t2 = t2, t1
    # fusion(t1, t2, 0, 2, 2)
    # print(t2)  # [1 2 3 4]

    taille = 1000000

    t1 = exo1.init_tab_random(taille, 5000000)

    tab_tri = tri_fusion(t1)
    print(tab_tri[100])  # 528
    print(tab_tri[808080])  # 4040168
