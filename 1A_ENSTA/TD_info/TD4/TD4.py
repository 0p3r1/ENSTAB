from math import sqrt

print("-----------------------------------------")
print("------------------ TD4 ------------------")
print("-----------------------------------------")

# ----------------------------------------
# -------------- EXERCICE 1 --------------
# ----------------------------------------

def ajoute_1():
    nb = int(input("Entrez un nombre : "))
    return print(nb + 1)

# ajoute_1()

# ----------------------------------------
# -------------- EXERCICE 2 --------------
# ----------------------------------------

def puissances(x):
    result = [x**i for i in range(1, 5)]
    return print(result, result[2])

# puissances(2)

# ----------------------------------------
# -------------- EXERCICE 3 --------------
# ----------------------------------------

def nbpattes():
    p = int(input("Entrez le nombre de poulets : "))
    v = int(input("Entrez le nombre de vaches : "))
    c = int(input("Entrez le nombre de canards : "))
    return print(2 * p + 4 * v + 2 * c)

# nbpattes()

# ----------------------------------------
# -------------- EXERCICE 4 --------------
# ----------------------------------------

def f_trinome(a, b, c, x):
    return print(a * x**2 + b * x + c)

# f_trinome(1, -2, 1, 1)

# ----------------------------------------
# -------------- EXERCICE 5 --------------
# ----------------------------------------

def f2(x):
    return x + 1

def f3(x, f):
    return print(f(x) * 2)

# f3(4, f2)

# ----------------------------------------
# -------------- EXERCICE 6 --------------
# ----------------------------------------

def somme_carres():
    n = int(input("Entrez un nombre entier : "))
    return print(sum(i**2 for i in range(n + 1)))

# somme_carres()

# ----------------------------------------
# -------------- EXERCICE 7 --------------
# ----------------------------------------

def somme_carres_liste():
    n = int(input("Entrez un nombre entier : "))
    liste_sommes = []
    somme = 0
    for i in range(n + 1):
        somme += i**2
        liste_sommes.append(somme)
    return print(liste_sommes)

# somme_carres_liste()

# ----------------------------------------
# -------------- EXERCICE 8 --------------
# ----------------------------------------

def suite_mystere():
    n = int(input("Entrez un nombre n : "))
    somme = 0
    for i in range(1, n + 1):
        somme += 1 / sqrt(i)
    return print(6 * somme)

# suite_mystere()

# ----------------------------------------
# -------------- EXERCICE 9 --------------
# ----------------------------------------

def trouve_min():
    liste = list(map(int, input("Entrez des nombres séparés par des espaces : ").split()))
    return print(min(liste))

# trouve_min()

def trouve_pairs():
    liste = list(map(int, input("Entrez des entiers séparés par des espaces : ").split()))
    return print([x for x in liste if x % 2 == 0])

# trouve_pairs()
