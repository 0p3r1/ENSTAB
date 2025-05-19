# --------------------------------------------------
# -------------- EXERCICE 2 // FIPA 27 -------------
# --------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

tab = np.load("tableau_ex2.npy")


def question1():
    dim_tab = np.ndim(tab)
    min_tab = np.min(tab)
    max_tab = np.max(tab)

    return print(
        f"Dimension du tableau : {dim_tab} \nMinimum : {min_tab} \nMaximum : {max_tab}"
    )


# question1()


def gauss2d(x, y):
    return np.exp(-((x**2 + y**2) / 2))


def question2():
    x = np.linspace(-1, 1, 1000)
    y = np.linspace(-1, 1, 1000)
    X, Y = np.meshgrid(x, y)
    G2D = gauss2d(X, Y)

    G2D_max = np.max(G2D)
    G2D[G2D > 0.8 * G2D_max] = 0

    return X, Y, G2D


# question2()


def question3():
    X, Y, G2D = question2()

    plt.figure()
    plt.imshow(G2D, extent=[-1, 1, -1, 1], cmap="autumn")
    plt.contour(X, Y, G2D)
    plt.imshow(tab, extent=[-1, 1, -1, 1], cmap="viridis", zorder=2)
    plt.colorbar()
    plt.title("Question 3")
    plt.show()


question3()
