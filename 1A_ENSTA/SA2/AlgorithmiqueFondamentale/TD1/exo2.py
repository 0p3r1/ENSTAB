import numpy as np
import exo1


def tri_insertion(tab):
    for i in range(len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j - 1] > x:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = x
    return tab


if __name__ == "__main__":
    tab = exo1.init_tab_random(10000, 20000)
    tab_tri = tri_insertion(tab)
    print(tab_tri[9090])
