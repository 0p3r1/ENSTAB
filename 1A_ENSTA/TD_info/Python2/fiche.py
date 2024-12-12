# --------------------------------------------------
# -------------------- PYTHON 2 --------------------
# --------------- OUTILS NUMÉRIQUES ----------------
# --------------------------------------------------

# Importation de la bibiliothèque
import numpy as np

# --------------------------------------------------
# -------------- CRÉATION DE TABLEAUX --------------
# --------------------------------------------------

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

# Création d'un tableau de X lignes et Y colonnes rempli de valeurs aléatoires comprises entre 0 et 1
tab_random = np.random.rand(1, 2)
# print(tab_random) -> Out : [[0.59403264 0.36494216]]

# --------------------------------------------------
# ------------ MANIPULATION DE TABLEAUX ------------
# --------------------------------------------------

# Élement de la première ligne/colonne du tableau tab_1D
premier_element_tab_1D = tab_1D[0]  # 0 : 1e ligne/colonne
# print(premier_element_tab_1D) -> Out : 1

# Élement de la X ligne et Y colonne du tableau tab_1D
element_tab_2D = tab_2D[0, 1]  # 0 : 1e ligne ; 1 : 2e colonne
# print(element_tab_2D) -> Out : 2

# 3 premiers élements du tableau tab_1D
tab_1D_3premiers = tab_1D[:3]
# print(tab_1D_3premiers) -> Out : [1 2 3]

# 2 derniers élements du tableau tab_1D
tab_1D_2derniers = tab_1D[-2:]
# print(tab_1D_2derniers) -> Out : [5 6]

# Sélection de la deuxième colonnne du tableau tab_2D
tab_2D_colonne2 = tab_2D[:, 1]
# print(tab_2D_colonne2) -> Out : [2 5]

# Sélection de la dernière colonne du tableau tab_2D
tab_2D_dercolonne = tab_2D[:, -1]
# print(tab_2D_dercolonne) -> Out : [3 6]

# --------------------------------------------------
# ------------- PROPRIÉTÉS DES TABLEAUX ------------
# --------------------------------------------------

# Forme du tableau -> renvoie un tuple (X,Y) : X lignes et Y colonnes
forme_tab2D = tab_2D.shape
# print(forme_tab2D) -> Out : (2, 3)

# Nb éléments du tableau -> renvoie le nb d'élements ds le tableau
nb_elements_tab2D = tab_2D.size
# print(nb_elements_tab2D) -> Out : 6
