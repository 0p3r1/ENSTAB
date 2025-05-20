import numpy as np


def init_tab_random(n=10, m=100, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, m, size=n)


if __name__ == "__main__":
    tab = init_tab_random(1000, 1000)
    print(tab, "\nSomme :", sum(tab))
