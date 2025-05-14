# *******************************************************
# ****************** ANALYSE NUMERIQUE ******************
# ************************* TD1 *************************
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x**3 - x


def F1(x):
    return (x**4) / 4 - (x**2) / 2


# *******************************************************
# ******* 1.3 Tracer les fonctions et les erreurs *******
# *******************************************************

# Question 9


def Ferr1(x, n):
    return F1(x) + x / n


def Ferr2(x, n):
    return F1(x) + x / (n**2)


def Ferr3(x, n):
    return F1(x) + x * np.cos(np.log(n)) / (n**2)


# Question 10 et 11

n_values = np.arange(1, 50000)
x = 3
F1_3 = F1(x)

ferr1_values = Ferr1(x, n_values)
ferr2_values = Ferr2(x, n_values)
ferr3_values = Ferr3(x, n_values)

plt.figure()

# plt.plot(n_values, ferr1_values, label="Ferr1")  # Question 10
# plt.plot(n_values, ferr2_values, label="Ferr2")  # Question 10
# plt.plot(n_values, ferr3_values, label="Ferr3")  # Question 10

plt.semilogx(n_values, ferr1_values, label="Ferr1")  # Question 11
plt.semilogx(n_values, ferr2_values, label="Ferr2")  # Question 11
plt.semilogx(n_values, ferr3_values, label="Ferr3")  # Question 11

plt.axhline(y=F1_3, color="black", linestyle="--", label="F1(3)")
plt.xlabel("n")
plt.ylabel("Valeur approchée de F1(3)")
plt.title("Ferr_k(3, n) vs n")
plt.legend()
plt.grid(True)
plt.show()

# Question 12

error1 = np.abs(ferr1_values - F1_3)
error2 = np.abs(ferr2_values - F1_3)
error3 = np.abs(ferr3_values - F1_3)

plt.figure()
plt.loglog(n_values, error1, label="Erreur Ferr1")
plt.loglog(n_values, error2, label="Erreur Ferr2")
plt.loglog(n_values, error3, label="Erreur Ferr3")
plt.xlabel("n (log)")
plt.ylabel("Erreur (log)")
plt.title("Erreur de Ferrk(3, n) vs n (log-log)")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()


# *******************************************************
# ******* 1.4 Schéma d'intégration par rectangles *******
# *******************************************************

# Question 13


def rectangleGauche(a, b, n, f):
    pas = (b - a) / n
    I = 0
    for i in range(n):
        ai = a + i * pas
        I += f(ai)
    return I * pas


def rectangleDroite(a, b, n, f):
    pas = (b - a) / n
    I = 0
    for i in range(n):
        ai = a + (i + 1) * pas
        I += f(ai)
    return I * pas


def rectangleCentre(a, b, n, f):
    pas = (b - a) / n
    I = 0
    for i in range(n):
        ai = a + (i + 0.5) * pas
        I += f(ai)
    return I * pas


# Question 14

a = 0
b = 3
n = 100

I_exacte = F1(b) - F1(a)

I_gauche = rectangleGauche(a, b, n, f1)
I_droite = rectangleDroite(a, b, n, f1)
I_centre = rectangleCentre(a, b, n, f1)

print("Valeur exacte :", I_exacte)
print("Rectangle gauche :", I_gauche)
print("Rectangle droite :", I_droite)
print("Rectangle centre :", I_centre)

# Question 15

n_vals = np.logspace(1, 5, 50, dtype=int)
err_g = []
err_d = []
err_c = []

for n in n_vals:
    err_g.append(abs(rectangleGauche(a, b, n, f1) - I_exacte))
    err_d.append(abs(rectangleDroite(a, b, n, f1) - I_exacte))
    err_c.append(abs(rectangleCentre(a, b, n, f1) - I_exacte))

plt.figure()
plt.loglog(n_vals, err_g, label="Erreur Gauche")
plt.loglog(n_vals, err_d, label="Erreur Droite")
plt.loglog(n_vals, err_c, label="Erreur Centre")
plt.xlabel("n (log)")
plt.ylabel("Erreur (log)")
plt.title("Erreur des méthodes rectangles vs n")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
