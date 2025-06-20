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

# plt.plot(t, y_exact, label="Solution exacte")
# plt.xlabel("Temps t")
# plt.ylabel("y(t)")
# plt.title("Solution exacte de l'équation $y'(t) = -ay(t)$")
# plt.legend()
# plt.grid()
# plt.show()

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
 
# print(euler(t0, tmax, h, y0, f))

# *******************************************************
# ** 4. Comparer les valeurs générées par euler et les
# ** valeurs exactes pour différentes valeurs de h. En
# ** déduire la précision de la méthode. On considère a=1
# ** Interpréter ce qui se passe pr h ∈]1, 2] et pr h > 2
# *******************************************************


# *******************************************************
# ** 5. En Python, créez une fonction d’évolution qui
# ** donne le vecteur (x'(t), y'(t)) en fonction du point
# ** (x(t), y(t)). Sur le modèle de la fonction de la
# ** question 2, elle pourra prendre en entrée pour y
# ** et pour sortie un numpy array monodimensionnel.
# *******************************************************

# (x'(t), y'(t))
# = (x(t)(a-by(t)), -y(t)(c-dx(t)))

def lotka_volterra(t, vect):
    x, y = vect
    xdot = x * (4 - 3 * y)
    ydot = -y * (3 - 2 * x)
    return np.array([xdot, ydot])

def question5():
    t = 0
    vect = np.array([2, 1/4])

    print(lotka_volterra(t, vect))

# *******************************************************
# ** 6. Au besoin, transformez la fonction euler()
# ** mono-dimensionnelle pour qu’elle puisse accepter
# ** cette fonction d’´evolution. La fonction doit renvoyer
# ** un tableau avec autant de lignes que la dimension du
# ** vecteur d’´etat, et autant de colonnes que de pas de
# ** temps. Affichez les courbes des populations de proies
# ** et de prédateurs.
# *******************************************************

def euler_evol(t0, tmax, h, y0, f):
    T = [t0]
    Y = [y0]
    t = t0
    y = y0.copy()

    while t < tmax:
        y = y + h * f(t, y)
        t += h
        T.append(t)
        Y.append(y.copy())

    return np.array(T), np.array(Y)

def question6():
    t0 = 0
    tmax = 20
    h = 0.01
    vect = np.array([2, 1/4])

    T, Y = euler_evol(t0, tmax, h, vect, lotka_volterra)

    axe_x = Y[:,0]
    axe_y = Y[:,1]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(axe_x, axe_y, label="")
    axes[0].set_title("LA PATATE")
    axes[0].set_xlabel("x(t) : proies")
    axes[0].set_ylabel("y(t) : prédateurs")
    axes[0].legend()

    axes[1].plot(T, axe_x, label="")
    axes[1].plot(T, axe_y, label="")
    axes[1].set_title("")
    axes[1].set_xlabel("Temps t")
    axes[1].set_ylabel("Population")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

# *******************************************************
# ** 9. Ecrire un schéma de Runge-Kutta pour remplacer le
# ** schéma d’Euler de la question 3. Reprendre la q4.
# *******************************************************

def rk2(t0, tmax, h, y0, f):
    T = [t0]
    Y = [y0.copy()]
    t = t0
    y = y0.copy()

    while t < tmax:
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y = y + h * (0.5 * k1 + 0.5 * k2)
        t = t + h
        T.append(t)
        Y.append(y.copy())

    return np.array(T), np.array(Y)

def question9():
    t0 = 0
    tmax = 20
    h = 0.01
    vect = np.array([2, 1/4])

    T, Y = euler_evol(t0, tmax, h, vect, lotka_volterra)
    T_RK2, Y_RK2 = rk2(t0, tmax, h, vect, lotka_volterra)

    axe_x = Y[:,0]
    axe_y = Y[:,1]

    axe_x_rk2 = Y_RK2[:,0]
    axe_y_rk2 = Y_RK2[:,1]

    fig, axes = plt.subplots(2, 2, figsize=(16, 8))

    axes[0, 0].plot(axe_x, axe_y, label="")
    axes[0, 0].set_title("EULER : LA PATATE")
    axes[0, 0].set_xlabel("x(t) : proies")
    axes[0, 0].set_ylabel("y(t) : prédateurs")
    axes[0, 0].legend()

    axes[0, 1].plot(T, axe_x, label="")
    axes[0, 1].plot(T, axe_y, label="")
    axes[0, 1].set_title("EULER")
    axes[0, 1].set_xlabel("Temps t")
    axes[0, 1].set_ylabel("Population")
    axes[0, 1].legend()

    axes[1, 0].plot(axe_x_rk2, axe_y_rk2, label="")
    axes[1, 0].set_title("RK2 : LA PATATE")
    axes[1, 0].set_xlabel("x(t) : proies")
    axes[1, 0].set_ylabel("y(t) : prédateurs")
    axes[1, 0].legend()

    axes[1, 1].plot(T_RK2, axe_x_rk2, label="")
    axes[1, 1].plot(T_RK2, axe_y_rk2, label="")
    axes[1, 1].set_title("RK2")
    axes[1, 1].set_xlabel("Temps t")
    axes[1, 1].set_ylabel("Population")
    axes[1, 1].legend()

    plt.tight_layout()
    plt.show()

# *******************************************************
# ** 14. Ecrire un schéa de Runge-Kutta d’ordre 3 et
# ** comparer le résultat obtenu avec les schémas
# ** précédents.
# *******************************************************

def rk3(t0, tmax, h, y0, f):
    T = [t0]
    Y = [y0.copy()]
    t = t0
    y = y0.copy()

    while t < tmax:
        k1 = f(t, y)
        k2 = f(t + h/3, y + (h/3) * k1)
        k3 = f(t + 2*h/3, y + (2*h/3) * k2)

        y = y + (h/4) * (k1 + 3*k3)
        t = t + h
        T.append(t)
        Y.append(y.copy())

    return np.array(T), np.array(Y)

def question14():
    t0 = 0
    tmax = 20
    h = 0.01
    vect = np.array([2, 1/4])

    T, Y = euler_evol(t0, tmax, h, vect, lotka_volterra)
    T_RK2, Y_RK2 = rk2(t0, tmax, h, vect, lotka_volterra)
    T_RK3, Y_RK3 = rk3(t0, tmax, h, vect, lotka_volterra)

    axe_x = Y[:,0]
    axe_y = Y[:,1]

    axe_x_rk2 = Y_RK2[:,0]
    axe_y_rk2 = Y_RK2[:,1]

    axe_x_rk3 = Y_RK3[:,0]
    axe_y_rk3 = Y_RK3[:,1]

    fig, axes = plt.subplots(3, 2, figsize=(16, 8))

    axes[0, 0].plot(axe_x, axe_y, label="")
    axes[0, 0].set_title("EULER : LA PATATE")
    axes[0, 0].set_xlabel("x(t) : proies")
    axes[0, 0].set_ylabel("y(t) : prédateurs")
    axes[0, 0].legend()

    axes[0, 1].plot(T, axe_x, label="")
    axes[0, 1].plot(T, axe_y, label="")
    axes[0, 1].set_title("EULER")
    axes[0, 1].set_xlabel("Temps t")
    axes[0, 1].set_ylabel("Population")
    axes[0, 1].legend()

    axes[1, 0].plot(axe_x_rk2, axe_y_rk2, label="")
    axes[1, 0].set_title("RK2 : LA PATATE")
    axes[1, 0].set_xlabel("x(t) : proies")
    axes[1, 0].set_ylabel("y(t) : prédateurs")
    axes[1, 0].legend()

    axes[1, 1].plot(T_RK2, axe_x_rk2, label="")
    axes[1, 1].plot(T_RK2, axe_y_rk2, label="")
    axes[1, 1].set_title("RK2")
    axes[1, 1].set_xlabel("Temps t")
    axes[1, 1].set_ylabel("Population")
    axes[1, 1].legend()

    axes[2, 0].plot(axe_x_rk3, axe_y_rk3, label="")
    axes[2, 0].set_title("RK3 : LA PATATE")
    axes[2, 0].set_xlabel("x(t) : proies")
    axes[2, 0].set_ylabel("y(t) : prédateurs")
    axes[2, 0].legend()

    axes[2, 1].plot(T_RK3, axe_x_rk3, label="")
    axes[2, 1].plot(T_RK3, axe_y_rk3, label="")
    axes[2, 1].set_title("RK3")
    axes[2, 1].set_xlabel("Temps t")
    axes[2, 1].set_ylabel("Population")
    axes[2, 1].legend()


    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    question14()