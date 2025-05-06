# ---------------------
# ENONCE
# ---------------------

# Soit la suite (Un) n ∈ N définie par u0 = 1 et ∀n ∈ N∗ , un = 3un−1 + 2.

# Écrire une fonction récursive suite(n) qui renvoie le terme un.


def suite(n):
    if n == 0:
        return 1
    else:
        return 3 * suite(n - 1) + 2
