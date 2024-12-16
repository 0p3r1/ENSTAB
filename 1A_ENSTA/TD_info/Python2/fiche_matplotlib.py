# --------------------------------------------------
# -------------------- PYTHON 2 --------------------
# --------------- OUTILS NUMÉRIQUES ----------------
# --------------------------------------------------
# ---------------- FICHE MATPLOTLIB ----------------
# --------------------------------------------------

# Importation des bibliothèques
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# -------------- BASES DE MATPLOTLIB ---------------
# --------------------------------------------------

# Création d'une figure
plt.figure()

# Affichage du graphique
plt.show()

# Enregistrement du graphique
plt.savefig("graph.png")  # Enregistrer au format PNG
plt.savefig("graph.png", transparent=True)  # Enregistrer avec fond transparent

# Nettoyage
plt.cla()  # Efface les tracés dans un axe (axes)
plt.clf()  # Efface toute la figure
plt.close()  # Ferme la fenêtre

# --------------------------------------------------
# ------------------ TRACÉ SIMPLE ------------------
# --------------------------------------------------

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Courbe de sin(x)")
plt.legend()
plt.show()

# --------------------------------------------------
# ---------------- TRACÉS MULTIPLES ----------------
# ---------------- SUR UN GRAPHIQUE ----------------
# --------------------------------------------------

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="sin(x)", color="blue")  # Courbe en bleue
plt.plot(
    x, y2, label="cos(x)", linestyle="dashed", color="red"
)  # Courbe en rouge et hachurée
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Courbe de sin(x) et cos(y)")
plt.legend()
plt.show()

# --------------------------------------------------
# ---------------- TRACÉS MULTIPLES ----------------
# ------------ SUR PLUSIEURS GRAPHIQUES ------------
# --------------------------------------------------

# Création d'une figure d'1 ligne et 2 colonnes de taille 12, 4
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

x = np.linspace(0, 10, 100)

# Graphique 1
y_axe1 = np.sin(x)
axes[0].plot(x, y_axe1, label="sin(x)")
axes[0].set_title("Graphique 1: sin(x)")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend()

# Graphique 2
y_axe2 = np.sin(x)
axes[1].plot(x, y_axe2, label="cos(x)")
axes[1].set_title("Graphique 2: cos(x)")
axes[1].set_xlabel("Temps (t)")
axes[1].set_ylabel("Amplitude")
axes[1].legend()

plt.tight_layout()
plt.show()

# --------------------------------------------------
# ------------------- ANNOTATIONS ------------------
# --------------------------------------------------

plt.plot(x, y, label="sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Courbe de sin(x) avec annotation")
# Annotation de "Point particulier" au point np.pi/2 de la courbe
plt.annotate(
    "Point particulier",
    xy=(np.pi / 2, 1),
    xytext=(np.pi, 0.5),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.legend()
plt.show()

# --------------------------------------------------

# Écriture du texte "Texte" en rouge et police 12 au point x=2 et y=0.5
plt.text(2, 0.5, "Texte", fontsize=12, color="red")
plt.show()

# --------------------------------------------------
# --------- PERSONALISATION DES GRAPHIQUES ---------
# --------------------------------------------------

# Limitations des axes
plt.xlim(0, 10)  # Limiter l'axe X de 0 à 10
plt.ylim(-1, 1)  # Limiter l'axe Y de -1 à 1

# Personalisation d'une courbe en violet, hachurée, etc..
plt.plot(x, y, color="purple", linestyle="dotted", linewidth=2, marker="o")

# Affichage d'une grille sur le graphique
plt.grid(True, linestyle="--", color="gray", alpha=0.6)

# --------------------------------------------------
# ------------- ENSEMBLE DE MANDELBROOT ------------
# --------------------------------------------------

x = np.linspace(-2.1, 0.6, 100)
y = np.linspace(-1.2, 1.2, 100)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C, dtype=complex)
N = np.zeros_like(C, dtype=int)

# Calcul de l'ensemble de Mandelbrot
max_iter = 100
for n in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    N[mask] += 1
N[N == max_iter] = 0

# Affichage de l'ensemble de Mandelbrot
plt.figure(figsize=(10, 8))
plt.imshow(N, extent=(-2.1, 0.6, -1.2, 1.2), cmap="turbo", origin="lower")
plt.colorbar()
plt.title("Ensemble de Mandelbrot")
plt.show()
