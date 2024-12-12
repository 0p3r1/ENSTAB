# --------------------------------------------------
# -------------------- PYTHON 2 --------------------
# --------------- OUTILS NUMÉRIQUES ----------------
# --------------------------------------------------

# Importation de la bibiliothèque
import numpy as np

# Création d'un tableau 1D
tab_1D = np.array([1, 2, 3, 4, 5, 6])
# print(tab_1D) -> Out : [1 2 3 4 5 6]

# Création d'un tableau 2D
tab_2D = np.array([[1, 2, 3], [4, 5, 6]])
# print(tab_2D) -> Out : [[1 2 3]
#                         [4 5 6]]

# Création d'un tableau de X lignes et Y colonnes rempli de 0 en float
tab_zero = np.zeros((1, 2))
# print(tab_zero) -> Out : [[0. 0.]]

# Création d'un tableau de X lignes et Y colonnes rempli de 1 en float
tab_un = np.ones((1, 2))
# print(tab_un) -> Out : [[1. 1.]]

# Création d'un tableau de X lignes et Y colonnes rempli de valeurs aléatoires comprises entre 0 et 1 en float
tab_random = np.random.rand(1, 2)
# print(tab_random) -> Out : [[0.59403264 0.36494216]]
