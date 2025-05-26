# *******************************************************
# ****************** ANALYSE NUMERIQUE ******************
# ************************* TD2 *************************
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt

# *******************************************************
# ***** 1. Donner la solution exacte de l’´equation *****
# *******************************************************

a = 1
t = np.linspace(0, 5, 100)

y_exact = np.exp(-a * t)

plt.plot(t, y_exact, label="Solution exacte")
plt.xlabel("Temps t")
plt.ylabel("y(t)")
plt.title("Solution exacte de l'équation $y'(t) = -ay(t)$")
plt.legend()
plt.grid()
plt.show()

# *******************************************************
# ** 2. Ecrire la fonction de dynamique de l’équation
# ** différentielle, sur papier et sur Python.
# ** On l’appellera f(t, y), mˆeme si t n’intervient pas.
# *******************************************************

def f(t,y = 1):
    a = 2
    return -a * y

# *******************************************************
# ** 3. Ecrire une fonction euler(t0, tmax, h, y0, f)
# ** qui renvoit un vecteur toutes les valeurs prises par
# ** yk dans la suite générée par un schéma d’Euler.
# *******************************************************

def euler(t0, tmax, h, y0, f):
    T = np.arange(t0, tmax + h, h)
    Y = []
    y = y0
    for t in T:
        Y.append(y)
        y = y + h * f(t, y)
    return np.array(Y)
 
t0 = 0
tmax = 5
h = 0.1
y0 = 1
 
print(euler(t0, tmax, h, y0, f))