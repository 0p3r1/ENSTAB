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