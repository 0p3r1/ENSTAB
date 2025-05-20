import numpy as np
import exo1


def tri_insertion_gap(tab, gap):
    for i in range(gap, len(tab)):
        x = tab[i]
        j = i
        while j >= gap and tab[j - gap] > x:
            tab[j] = tab[j - gap]
            j -= gap
        tab[j] = x
    return tab


def shell_sort(tab):
    n = len(tab)
    gap = 1
    gaps = []

    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    gaps.reverse()

    for g in gaps:
        tri_insertion_gap(tab, g)

    return tab


if __name__ == "__main__":
    tab = exo1.init_tab_random(100000, 500000)
    shell_sort(tab)
    print(tab[80808])
