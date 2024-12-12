# ----------------------------------------
# -------------- EXERCICE 1 --------------
# ----------------------------------------

def exercice1():
    liste_nombres = [15, 34, 89, 33, 11, 28, 18, 981, 42, 12, 69]

    min = liste_nombres[0]
    max = liste_nombres[0]
    sum = 0

    for i in range(len(liste_nombres)):
        if liste_nombres[i] < min:
            min = liste_nombres[i]
        elif liste_nombres[i] > max:
            max = liste_nombres[i]
        sum += liste_nombres[i]
    sum = sum/len(liste_nombres)

    question1 = print("Min : ", min, "\nMax : ", max, "\nSum : ", sum)

    multipesTrois = []

    for i in range(len(liste_nombres)):
        if liste_nombres[i] % 3 == 0:
            multipesTrois.append(liste_nombres[i])

    question2 = print("Multiples de 3 présents dans liste_nombres : ", multipesTrois)

    return question1, question2

# exercice1()

# ----------------------------------------
# -------------- EXERCICE 2 --------------
# ----------------------------------------

def temps_de_vol(h):
    u0 = h

    syracuse_liste = []
    syracuse_liste.append(u0)

    count=0

    while syracuse_liste[-1] != 1:
        if syracuse_liste[-1] % 2 == 0:
            syracuse_liste.append(syracuse_liste[-1] // 2)
        elif syracuse_liste[-1] % 2 != 0:
            syracuse_liste.append((syracuse_liste[-1] * 3) + 1)
        count+=1

    return count

def exercice2():
    h = int(input("Entrez la valeur de u0 : "))
    iterations = int(input("Entrez le nombre d'iterations souhaités : "))

    u0 = h

    if u0 % 2 == 0:
        question1 = print("Pour u0 = ", u0, " on a u(n+1) = ", u0 // 2)
    elif u0 % 2 != 0:
        question1 = print("Pour u0 = ", u0, " on a u(n+1) = ", (u0 * 3) + 1)
    else:
        question1 = ""

    syracuse_liste = []

    syracuse_liste.append(u0)

    for i in range(iterations):
        if syracuse_liste[-1] % 2 == 0:
            syracuse_liste.append(syracuse_liste[-1]//2)
        elif syracuse_liste[-1] % 2 != 0:
            syracuse_liste.append((syracuse_liste[-1]*3)+1)

    question2 = print("Pour u0 = ", u0, " et pour ", iterations, "iterations on a ", syracuse_liste)
    question3 = print("Temps de vol :", temps_de_vol(h))

    plusGrandTempsVol = 0
    valeurInitiale = 0

    for i in range(1, 101):
        if temps_de_vol(i) > plusGrandTempsVol:
            plusGrandTempsVol = temps_de_vol(i)
            valeurInitiale = i

    question4 = print("Plus grand temps de vol pour u0 de 1 à 100 :", plusGrandTempsVol, "pour une valeur initiale de : ", valeurInitiale)

    return question1, question2, question3, question4

exercice2()
