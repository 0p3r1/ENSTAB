# --------------------------------------------------
# -------------- EXERCICE 1 // FIPA 27 -------------
# --------------------------------------------------

import numpy as np
from numpy.random import randint as ri
import matplotlib.pyplot as plt

np.random.seed(42)
A = ri(0, ri(100), (ri(30, 42), ri(10, 30)))


def question1():
    nblignescol_A = np.shape(A)
    nbelements_A = np.size(A)

    return print(
        f"Il y a {nblignescol_A[0]} lignes et {nblignescol_A[1]} colonnes, soit {nbelements_A} éléments."
    )


# question1()


def verif_question1():
    nbelements_A = np.size(A)
    lignes = np.shape(A)[0]
    colonnes = np.shape(A)[1]

    nbelements_verif = lignes * colonnes

    return print(
        f"Il y a bien {nbelements_verif} éléments après avoir multipliés le nb de colonnes avec le nb de lignes."
    )


# verif_question1()


def question2():
    x = A[5, :]  # 6e ligne
    y = A[8, :]  # 9e ligne
    plt.plot(x, y, label="")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("")
    plt.show()


# question2()


def question3():
    X = np.linspace(1, 10, np.shape(A)[1])
    B = A[::2, :]
    B_moy = np.mean(B, axis=0)
    q4 = B_moy / X

    return print(X), print(B), print(B_moy), print(q4)


question3()
