# Question 1 : Que vaut 𝑆₁ ? Et 𝑆₀ ?

# 𝑆₁ = 1^3 = 1
# 𝑆₀ = 0

# Question 2 : Relation de récurrence

# 𝑆𝑛 = 𝑆𝑛-₁ + 𝑛^3

# Question 3 : Écrire une fonction récursive somme_cubes(n) qui prend en argument un nombre entier 𝑛 et qui calcule 𝑆𝑛.


def somme_cubes(n):
    if n == 0:
        return 0
    else:
        return somme_cubes(n - 1) + n**3
