# Écrivez une méthode récursive permettant de calculer le PGCD de deux entiers naturels par l'algorithme d'Euclide


def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


# Que vaut le PGCD entre 477865542 et 717173730 ?

if __name__ == "__main__":
    print(pgcd(477865542, 717173730))  # 4242
