# --------------------------------------------------
# -------------- EXERCICE 3 // FIPA 27 -------------
# --------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

img = np.load("tableau_ex3.npy")


def preliminaires():
    plt.figure()
    plt.imshow(img, extent=[-1, 1, -1, 1], cmap="gray")
    plt.colorbar()
    plt.title("Préliminaires")
    plt.show()


# preliminaires()


def norme(A, B):
    return np.sqrt(A**2 + B**2)


def nbpair(x):
    if x % 2 == 0:
        return True
    else:
        return False


def verifK(K):
    dim = np.shape(K)
    if dim[0] == dim[1]:
        if nbpair(dim[0]) == False:
            return True, dim[0]
        else:
            return False
    else:
        return False


def convolution(K, A):
    result, racinecarre = verifK(K)
    if result == True:
        taille = racinecarre // 2
        res = np.zeros(A.shape)
        indices = np.arange(-taille, taille + 1, 1)
        nb_l = np.shape(A)[0]
        nb_c = np.shape(A)[1]

        for i in range(taille, nb_l - taille):
            for j in range(taille, nb_c - taille):
                prod = A[i + indices, j + indices] * K
                somme = np.sum(prod)
                res[i, j] = somme
        return res


def question4():
    K = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    verif = convolution(K, img)
    verif = verif[:-1]  # On supprime la dernière ligne
    verif = verif[1:]  # On supprime la première ligne
    verif = verif[:, :-1]  # On supprime la dernière colonne
    verif = verif[:, 1:]  # On supprime la première colonne


# question4()


def question5():
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    contours_x = convolution(Gx, img)
    Gy = Gx.T
    contours_y = convolution(Gy, img)
    result = norme(contours_x, contours_y)
    plt.figure()
    plt.imshow(result, extent=[-1, 1, -1, 1], cmap="gray")
    plt.colorbar()
    plt.title("")
    plt.show()


question5()
