# Question 1 : Traduire cette définition en une fonction récursive fibonacci(n).s


def fibonacci(n):
    print("Appel avec n =", n)  # cf. question 3
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Question 2 : Tester la fonction fibonacci(n) en prenant des valeurs de n de plus en plus grandes, pas à pas, surtout en augmentant doucement à partir d’environ 30 (ne pas tester directement plus de 35). Que se passe-t-il ?

# if __name__ == "__main__":
#     for i in range(30):
#         print(fibonacci(i))

# Question 3 : Pour comprendre ce qui se passe, insérer au tout début de la fonction la ligne print("Appel avec n =", n) et ré-essayer, cette fois d’abord avec des tout petits nombres, comme 4, 5, 6. Expliquer ce que vous constatez

if __name__ == "__main__":
    liste_q3 = [4, 5, 6]
    for nb in liste_q3:
        print(fibonacci(nb))

# La fonction récursive fibonacci(n) recalcule plusieurs fois les mêmes sous-problèmes.
# C’est ce qu’on appelle une récursion avec duplication ou arbre d’appels exponentiel.

# Le nombre d'appels récursifs explose de manière exponentielle avec la valeur de n.
# C’est pourquoi la fonction devient très lente dès qu'on dépasse n ≈ 30.
