from itertools import count

print("-----------------------------------------")
print("------------------ TD2 ------------------")
print("-----------------------------------------")

# ----------------------------------------
# -------------- EXERCICE 1 --------------
# ----------------------------------------

def pariteNombre():
    nb = int(input("Entrez un nombre positif : "))

    if nb > 0 :
        bool = nb%2
        if bool == 0:
            return print("PAIR")
        elif bool == 1:
            return print("IMPAIR")

# pariteNombre()

# ----------------------------------------
# -------------- EXERCICE 2 --------------
# ----------------------------------------

def nbDivisibilite():
    nb = int(input("Entrez un nombre positif : "))

    if nb > 0 :
        count=0
        while nb%2 == 0:
            count+=1
            nb=nb//2
        return print("Le nombre " + str(nb) + " est divisible par 2 " + str(count) + " fois.")

# nbDivisibilite()

# ----------------------------------------
# -------------- EXERCICE 3 --------------
# ----------------------------------------

def multipleTrois():
    table = ""
    nb_ref = 7

    for i in range(1, 21):
        nb = nb_ref*i
        if nb%3 == 0:
            table+= str(nb) + "* "
        else:
            table+= str(nb) + " "
    return print(table)

# multipleTrois()

# ----------------------------------------
# -------------- EXERCICE 4 --------------
# ----------------------------------------

def nbFactorielles():
    nb = int(input("Entrez un nombre positif : "))

    if nb == 0:
        return print("1")
    elif nb > 0:
        nb_facto = 1
        for i in range(1, nb+1):
            nb_facto = nb_facto * i
        return print(len(str(nb_facto)))

# nbFactorielles()

# ----------------------------------------
# -------------- EXERCICE 5 --------------
# ----------------------------------------

def suiteFibonacci():
    x, y = 0, 1
    count = 0

    nb = 267914296

    while y < nb:
        z = x+y
        x = y
        y = z
        count += 1

    return print("Pour n = " + str(count) + ", on obtient " + str(nb))

# suiteFibonacci()

# ----------------------------------------
# -------------- EXERCICE 6 --------------
# ----------------------------------------

def calculPi():
    s=0
    for i in range(100000):
        u=(8*(-1)**i)/((2*i+1)*(2*i+3))
        s+=u
    valeur_pi = (s+4)/2
    return print(valeur_pi)

# calculPi()

# ----------------------------------------
# -------------- EXERCICE 7 --------------
# ----------------------------------------

def frequence():
    txt = str(input("Entrez une phrase : "))
    count=0
    for i in range(len(txt)):
        if txt[i].lower() == "y":
            count +=1
    return print(count)

# frequence()

# ----------------------------------------
# -------------- EXERCICE 8 --------------
# ----------------------------------------

def inverseString():
    txt = str(input("Entrez une phrase : "))
    txt_return = ""
    count=len(txt)
    for i in range(len(txt)):
        count -= 1
        txt_return += txt[count]
    return print(txt_return)

# inverseString()
