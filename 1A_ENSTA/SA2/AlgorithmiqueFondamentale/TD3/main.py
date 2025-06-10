# ========================================================================
# Étude du problème du sac à dos : Complexité et Algorithmes de résolution
# ========================================================================

import numpy as np

def sac_a_dos(objets, masse_max):
    n = len(objets)
    memoire = np.zeros((n + 1, masse_max + 1), dtype=int)
    selection = np.zeros((n + 1, masse_max + 1), dtype=bool)

    def recherche_recursive(i, capacite_restante):
        if i == 0 or capacite_restante == 0:
            return 0
        elif memoire[i, capacite_restante] != 0:
            return memoire[i, capacite_restante]
        elif objets[i - 1]['masse'] > capacite_restante:
            memoire[i, capacite_restante] = recherche_recursive(i - 1, capacite_restante)
            return memoire[i, capacite_restante]
        else:
            valeur_incluse = objets[i - 1]['valeur'] + recherche_recursive(i - 1, capacite_restante - objets[i - 1]['masse'])
            valeur_exclue = recherche_recursive(i - 1, capacite_restante)
            if valeur_incluse > valeur_exclue:
                memoire[i, capacite_restante] = valeur_incluse
                selection[i, capacite_restante] = True
            else:
                memoire[i, capacite_restante] = valeur_exclue
                selection[i, capacite_restante] = False
            return memoire[i, capacite_restante]

    recherche_recursive(n, masse_max)

    objets_selectionnes = []
    capacite_restante = masse_max
    for i in range(n, 0, -1):
        if selection[i, capacite_restante]:
            objets_selectionnes.append(objets[i - 1])
            capacite_restante -= objets[i - 1]['masse']

    valeur_maximale = memoire[n, masse_max]
    return valeur_maximale, objets_selectionnes 

if __name__ == "__main__":
    objets = [
        {'nom': 'Objet 1', 'masse': 2, 'valeur': 12},
        {'nom': 'Objet 2', 'masse': 1, 'valeur': 10},
        {'nom': 'Objet 3', 'masse': 3, 'valeur': 20},
        {'nom': 'Objet 4', 'masse': 2, 'valeur': 15}
    ]

    masse_max = 5
    valeur_maximale, objets_selectionnes = sac_a_dos(objets, masse_max)

    print(f"Valeur maximale : {valeur_maximale}")
    print("Objets sélectionnés :")
    for obj in objets_selectionnes:
        print(f"{obj['nom']} (Masse: {obj['masse']}, Valeur: {obj['valeur']})")