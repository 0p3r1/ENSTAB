# Question 1

# Écrire une fonction récursive fibo_malin(a, b, n) qui utilisera a et b comme accumulateurs pour calculer Fn en fonction Fn-1 et Fn-2, on décidera arbitrairement que a représente Fn-1 et b prendra le rôle de Fn-2. indice: l'appel récursif sera fibo_malin(a + b, a, ????).


def fibo_malin(a, b, n):
    if n == 0:
        return b
    else:
        return fibo_malin(a + b, a, n - 1)


if __name__ == "__main__":
    print(fibo_malin(1, 0, 998))


# Question 2

# La récursivité simplifie-t-elle encore la formulation dans ce cas ?

# Oui car elle évite les appels redondants et suit une logique simple et linéaire.

# Question 3

# Quel nom porte cette forme de récursivité ?

# Récursivité terminale.
