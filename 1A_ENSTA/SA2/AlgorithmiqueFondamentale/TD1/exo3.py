import numpy as np
import exo2


def shell_sort(tab):
    n = len(tab)
    gap = 1
    gaps = []

    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    gaps.reverse()

    for g in gaps:
        exo2.tri_insertion(tab, g)

    return tab


if __name__ == "__main__":
    tab = exo1.init_tab_random(100000, 500000)
    shell_sort(tab)
    print(tab[80808])
