print("-----------------------------------------")
print("------------------ TD3 ------------------")
print("-----------------------------------------")

# ----------------------------------------
# -------------- EXERCICE 1 --------------
# ----------------------------------------

def plusGrandElement(list):
    x = 0
    for i in range(len(list)):
        if list[i] > x:
            x = list[i]
    return print(x)

list = [32, 5, 12, 8, 3, 75, 2, 15]
# plusGrandElement(list)

# ----------------------------------------
# -------------- EXERCICE 2 --------------
# ----------------------------------------

def impairPairListes(list):
    listPair = []
    listImpair = []
    for i in range(len(list)):
        if list[i]%2 == 0:
            listPair.append(list[i])
        elif list[i]%2 == 1:
            listImpair.append(list[i])
    return print(listPair, listImpair)

# impairPairListes(list)

# ----------------------------------------
# -------------- EXERCICE 3 --------------
# ----------------------------------------

def notes():
    notes = []

    while True:
        note = int(input("Entrez une note : "))

        if note < 0:
            break

        notes.append(note)

    return print("Nb :", len(notes), "\nMax :", max(notes), "\nMin :", min(notes), "\nMoy :", (sum(notes)/len(notes)))

# notes()

# ----------------------------------------
# -------------- EXERCICE 4 --------------
# ----------------------------------------

def insertMonthDays():
    t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    t2 = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre', 'Novembre','Décembre']
    t3 = []

    if len(t1) == len(t2):
        for i in range(len(t1)):
            t3.append(t2[i])
            t3.append(t1[i])
    return print(t3)

# insertMonthDays()

# ----------------------------------------
# -------------- EXERCICE 5 --------------
# ----------------------------------------

def frequenceListeMots():
    mots = ['clochard', 'panier', 'excecrable', 'analphabete', 'bambou', 'caractere', 'lentilles', 'manteau', 'chaussettes', 'kirikou']

    letter = input("Entrez une lettre : ")
    letterMin = letter.lower()

    count_letters = 0
    count_mots = []

    for i in range(len(mots)):
        for j in range(len(mots[i])):
            if letterMin == mots[i][j]:
                count_letters += 1
                if mots[i] not in count_mots:
                    count_mots.append(mots[i])

    return print(count_letters, count_mots)

# frequenceListeMots()

# ----------------------------------------
# -------------- EXERCICE 6 --------------
# ----------------------------------------

def nbPremiers():
    lim = 1000
    list = [1] * (lim+1)

    list[0], list[1] = 0, 0

    for i in range(2, int(lim ** 0.5) + 1):
        if list[i] == 1:
            for j in range(i * i, lim + 1, i):
                list[j] = 0

    nombres_premiers = [i for i in range(2, lim + 1) if list[i] == 1]

    return print(nombres_premiers)

# nbPremiers()

# ----------------------------------------
# -------------- EXERCICE 7 --------------
# ----------------------------------------

def remplir_dictionnaire():
    dico = {}
    while True:
        nom = input("Entrez le nom (ou appuyez sur <Entrée> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = (age, taille)
    return dico

def consulter_dictionnaire(dico):
    while True:
        nom = input("Entrez le nom (ou appuyez sur <Entrée> pour terminer) : ")
        if nom == "":
            break
        elif nom in dico:
            age, taille = dico[nom]
            print("Nom : {} - âge : {} ans - taille : {} m.".format(nom, age, taille))
        else:
            print(f"{nom} n'est pas dans le dictionnaire.")

def systeme_bdd_dict():
    while True:
        choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ").lower()
        if choix == 'r':
            dictionnaire = remplir_dictionnaire()
        elif choix == 'c':
            consulter_dictionnaire(dictionnaire)
        elif choix == 't':
            break
        else:
            print("Choix invalide, veuillez entrer 'R', 'C', ou 'T'.")

# systeme_bdd_dict()
