import numpy as np


def init_tab_random(n=10, m=100, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, m, size=n)


def tab_croissant(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True


def plus_petite_graine(n=10, m=10):
    seed = 1
    while True:
        tab = init_tab_random(n, m, seed)
        if tab_croissant(tab):
            return seed, tab
        seed += 1


if __name__ == "__main__":
    seed, sorted_tab = plus_petite_graine()
    print(sorted_tab, "\nLa plus petite graine pour un tableau trié est :", seed)
