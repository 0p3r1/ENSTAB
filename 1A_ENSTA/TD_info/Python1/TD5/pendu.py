from utils.fonction import recup_lettre, choisir_mot, recup_mot_masque
from utils.donnees import nombre_chances

def jouer():
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    chances = nombre_chances

    print("Bienvenue dans le jeu du Pendu !")
    print(f"Le mot à trouver a {len(mot_a_trouver)} lettres.")

    while chances > 0:
        mot_masque = recup_mot_masque(mot_a_trouver, lettres_trouvees)
        print(f"Mot à deviner : {mot_masque}")
        print(f"Il vous reste {chances} chances.")

        lettre = recup_lettre()

        if lettre in lettres_trouvees:
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print("Bien joué !")
        else:
            chances -= 1
            print(f"... non, cette lettre ne se trouve pas dans le mot... Il vous reste {chances} chances.")

        if mot_a_trouver == mot_masque:
            print(f"Félicitations ! Vous avez trouvé le mot : {mot_a_trouver}")
            break
    else:
        print(f"PENDU !!! Vous avez perdu. Le mot était : {mot_a_trouver}")

    continuer = input("Voulez-vous continuer ? (o/n) : ").lower()
    if continuer == 'o':
        jouer()

# Lancer le jeu
if __name__ == "__main__":
    jouer()