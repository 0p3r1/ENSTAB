# --------------------------------------------------
# -------------------- PYTHON 2 --------------------
# --------------- OUTILS NUMÉRIQUES ----------------
# --------------------------------------------------
# ------------------ FICHE NUMPY -------------------
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

# Création d'un tableau de de 0 à 10 (exclu) par pas de 2
tab_arange = np.arange(0, 10, 2)
# print(tab_arange) -> Out : [0 2 4 6 8]

# Création d'un tableau de 5 valeurs équidistantes entre 0 et 10 (inclus)
tab_equidistants = np.linspace(0, 10, 5)
# print(tab_equidistants) -> Out : [ 0.   2.5  5.   7.5 10. ]

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

# Dimension du tableau -> renvoie la dimension du tableau
dim_tab2D = tab_2D.ndim
# print(dim_tab2D) -> Out : 2

# Type des éléments du tableau -> renvoie int, float, etc..
type_tab2D = tab_2D.dtype
# print(type_tab2D) -> Out : int64

# --------------------------------------------------
# ----------- OPÉRATIONS SUR LES TABLEAUX ----------
# --------------------------------------------------

# ----------- Rappel du contenu de tab_2D ----------
# print(tab_2D) -> Out : [[1 2 3]
#                         [4 5 6]]
# --------------------------------------------------

# -------------- Rappel des opérateurs -------------
# + -> addition
# - -> soustraction
# / -> division
# % -> modulo
# * -> multiplication
# ** -> exposant
# --------------------------------------------------

# Addition élément par élément
addition_tab_2D = tab_2D + 2
# print(addition_tab_2D) -> Out : [[3 4 5]
#                                  [6 7 8]]

# Addition de tableaux de MÊME DIMENSION
temp_tab_A = np.array([[1, 2, 3], [4, 5, 6]])
temp_tab_B = np.array([[2, 4, 6], [8, 9, 0]])
addition_tabs = temp_tab_A + temp_tab_B
# print(addition_tabs) -> Out : [[ 3  6  9]
#                                [12 14  6]]

# -------------- Rappel des fcts trigos ------------
# np.cos(x) -> cosinus
# np.sin(x) -> sinus
# np.tan(x) -> tangente
# np.arccos(x) -> arccosinus
# np.arcsin(x) -> arcsinus
# np.arctan(x) -> arctangente
# --------------------------------------------------

# Cosinus d'éléments d'un tableau
cos_tab2D = np.sin(tab_2D)
# print(cos_tab2D) -> Out : [[ 0.84147098  0.90929743  0.14112001]
#                            [-0.7568025  -0.95892427 -0.2794155 ]]

# ------------- Rappel des fcts diverses ------------
# np.sqrt(x) -> racine carrée
# np.exp(x) -> exponentielle
# np.log(x) -> log
# np.abs(x) -> valeur absolue
# np.sign(x) -> signe
# --------------------------------------------------

# Raciné carré d'éléments d'un tableau
sqrt_tab2D = np.sqrt(tab_2D)
# print(sqrt_tab2D) -> Out : [[1.         1.41421356 1.73205081]
#                             [2.         2.23606798 2.44948974]]

# --------------------------------------------------
# ------------- INFOS SUR LES TABLEAUX -------------
# --------------------------------------------------

# Somme des éléments du tableau
sum_tab2D = np.sum(tab_2D)
# print(sum_tab2D) -> Out : 21

# Moyenne des éléments du tableau
mean_tab2D = np.mean(tab_2D)
# print(mean_tab2D) -> Out : 3.5

# Minimum des éléments du tableau
min_tab2D = np.min(tab_2D)
# print(min_tab2D) -> Out : 1

# Maximum des éléments du tableau
max_tab2D = np.max(tab_2D)
# print(max_tab2D) -> Out : 6

# --------------------------------------------------
temp_mutmatri_tabA = np.array([[1, 2, 3], [4, 5, 6]])
temp_mutmatri_tabB = np.array([[4], [2], [1]])
# --------------------------------------------------

# Multiplication matricielle de deux tableaux
mulmatri_tab2D = temp_mutmatri_tabA @ temp_mutmatri_tabB
# print(mulmatri_tab2D) -> Out : [[11]
#                                 [32]]

# Transposition des éléments du tableau
transpo_tab2D = temp_mutmatri_tabA.T
# print(transpo_tab2D) -> Out : [[1 4]
#                                [2 5]
#                                [3 6]]

# --------------------------------------------------
# ----------- TRANSORMATIONS DE TABLEAUX -----------
# --------------------------------------------------

# ----------- Rappel du contenu de tab_1D ----------
# print(tab_1D) -> Out : [1 2 3 4 5 6]
# --------------------------------------------------

# Transforme le tableau tab_1D en 2x3
reshape_tab_1D = tab_1D.reshape(2, 3)
# print(reshape_tab_1D) -> Out : [[1 2 3]
#                                 [4 5 6]]

# Concaténation verticale de 2 tableaux de même forme
vert_tabs = np.concatenate((reshape_tab_1D, tab_2D), axis=0)
# print(vert_tabs) -> Out : [[1 2 3]
#                            [4 5 6]
#                            [1 2 3]
#                            [4 5 6]]

# Concaténation horizontale de 2 tableaux de même forme
hori_tabs = np.concatenate((reshape_tab_1D, tab_2D), axis=1)
# print(hori_tabs) -> Out : [[1 2 3 1 2 3]
#                           [4 5 6 4 5 6]]

# --------------------------------------------------
# ---------------------- BONUS ---------------------
# --------------------------------------------------

# Cela permet de trouver les coefficients du polynôme de degré deg qui s'ajuste le mieux aux points (x, y) selon la méthode des moindres carrés.

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])
deg = 2

coeffs = np.polyfit(x, y, deg)
# x : Les abscisses des points (tableau 1D)
# y : Les ordonnées des points (tableau 1D)
# deg : Le degré du polynôme

a, b, c = coeffs

print(f"Les coefficients du polynôme sont : a = {a}, b = {b}, c = {c}")
print(f"Le polynôme est de la forme : {a}x^2 + ({b})x + ({c})")

# Cela permet d'évaluer un polynôme défini par ses coefficients p pour des valeurs de x.
y = np.polyval(p, x)
# p : Coefficients du polynôme (généralement ceux retournés par np.polyfit)
# x : Valeurs de x où le polynôme doit être évalué
# y : Valeur de y du polynôme pour chaque x donné
