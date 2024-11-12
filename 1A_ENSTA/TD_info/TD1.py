from numpy import *

print("-----------------------------------------")
print("------------------ TD1 ------------------")
print("-----------------------------------------")

# ----------------------------------------
# -------------- EXERCICE 1 --------------
# ----------------------------------------

def volumeConeDroit():
    r = int(input("Entrez le rayon : "))
    h = int(input("Entrez la hauteur : "))

    v = (pi * (r ** 2) * h) / 3

    return print("Le volume du cône droit de rayon r=" + str(r) + " et de hauteur h=" + str(h) + " est v=" + str(v))

# volumeConeDroit()

# ----------------------------------------
# -------------- EXERCICE 2 --------------
# ----------------------------------------

def prixTTC():
    prixHT = float(input("Entrez le prix HT : "))
    TVA = float(input("Entrez la TVA : "))

    if TVA > 1 :
        return print("Le prix TTC est : " + str(prixHT*(1+(TVA/100))))
    elif TVA <= 1:
        return print("Le prix TTC est : " + str(prixHT * (1 + TVA)))

# prixTTC()

# ----------------------------------------
# -------------- EXERCICE 3 --------------
# ----------------------------------------

def traceLigne():
    villeDepart = str(input("Entrez la ville de départ : "))
    villeArrivee = str(input("Entrez la ville d'arrivée : "))
    distance = int(input("Entrez la distance : "))

    return print(villeDepart + " x " + ("-" * distance) + " x " + villeArrivee)

# traceLigne()

# ----------------------------------------
# -------------- EXERCICE 4 --------------
# ----------------------------------------

def distanceGardien():
    marches = int(input("Combien de marches : "))
    h_marches = int(input("Hauteur d'une marche (cm) : "))

    allers_retours = 5

    distance_aller_retour = 2 * (marches * h_marches)
    distance_quotidienne = distance_aller_retour * allers_retours
    distance_hebdomadaire = 7 * distance_quotidienne

    return print("Pour " + str(marches) + " marches de " + str(h_marches) + " cm, il parcourt " + str(distance_hebdomadaire/100) + " m par semaine")

# distanceGardien()

# ----------------------------------------
# -------------- EXERCICE 5 --------------
# ----------------------------------------

def conversionSecToTimestamp():
    secondes = int(input("Nombre de secondes : "))

    secondes_par_heure = 3600
    secondes_par_jour = secondes_par_heure * 24
    secondes_par_mois = secondes_par_jour * 30
    secondes_par_an = secondes_par_jour * 365

    annees = secondes // secondes_par_an
    secondes %= secondes_par_an

    mois = secondes // secondes_par_mois
    secondes %= secondes_par_mois

    jours = secondes // secondes_par_jour
    secondes %= secondes_par_jour

    heures = secondes // secondes_par_heure
    secondes %= secondes_par_heure

    minutes = secondes // 60
    secondes %= 60

    return print(str(annees) + " an(s) " + str(mois) + " mois " + str(jours) + " jour(s) " + str(heures) + " heure(s) " + str(minutes) + " minute(s) " + str(secondes) + " seconde(s)")

# conversionSecToTimestamp()

# ----------------------------------------
# -------------- EXERCICE 6 --------------
# ----------------------------------------

def conversionDegToRad():
    angle_degres = int(input("Angle (en degrés) : "))
    angle_minutes = int(input("Minutes : "))
    angle_secondes = int(input("Secondes : "))

    if 0 <= angle_minutes < 60 and 0 <= angle_secondes < 60:
        total_degres = angle_degres + angle_minutes / 60 + angle_secondes / 3600
        radians = total_degres * (pi / 180)
        return print(f"L'angle en radians est : {radians:.6f}")

# conversionDegToRad()

# ----------------------------------------
# -------------- EXERCICE 7 --------------
# ----------------------------------------

def conversionCelsiusToFahrenheit():
    choix = int(input("Entrez un choix entre : \n 1. Vers Celsius \n 2. Vers Fahrenheit \n Choix : "))
    temperature = float(input("Entrez une température : "))

    if choix == 1:
        celsius = (temperature - 32)/1.8
        return print(str(temperature) + "°F correspond à " + str(celsius) + "°C")
    elif choix == 2:
        fahrenheit = temperature*1.8 + 32
        return print(str(temperature) + "°C correspond à " + str(fahrenheit) + "°F")

# conversionCelsiusToFahrenheit()

# ----------------------------------------
# -------------- EXERCICE 8 --------------
# ----------------------------------------

def conversionMilesToKilometers():
    vitesseMiles = float(input("Entrez une vitesse en miles/heure : "))

    vitesseKilometers = vitesseMiles * 1.609

    vitesseMeters = vitesseKilometers / 3.6

    return print(str(vitesseMiles) + " miles/h correspond à " + str(round(vitesseKilometers, 2)) + "km/h et à " + str(round(vitesseMeters,2)) + " m/s")

# conversionMilesToKilometers()
