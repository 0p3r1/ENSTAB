import numpy as np


def init_tab_random(n=1000, m=1000, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, m, size=n)


if __name__ == "__main__":
    tab = init_tab_random()
    print(tab, "\nSomme :", sum(tab))
