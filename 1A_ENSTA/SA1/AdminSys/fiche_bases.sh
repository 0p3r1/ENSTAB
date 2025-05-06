# --------------------------------------------------
# -------------------- ADMIN SYS -------------------
# ---------------------- SHELL ---------------------
# --------------------------------------------------

# --------------------------------------------------
# ---------------- COMMANDES DE BASE ---------------
# --------------------------------------------------

# Affiche l'utilisateur actuel
whoami

# Affiche la date et l'heure actuelles
date

# Affiche la liste des fichiers et dossiers du répertoire courant
ls

# Change de répertoire
cd /chemin/vers/dossier

# Affiche le répertoire courant
pwd

# Crée un dossier
mkdir nom_du_dossier

# Supprime un fichier
rm nom_du_fichier

# Supprime un dossier et son contenu
rm -rf nom_du_dossier

# Affiche le contenu d'un fichier
cat nom_du_fichier

# Copie un fichier ou un dossier
# -r : Recopie récursive des dossiers et de leur contenu
cp -r source destination

# Déplace ou renomme un fichier ou un dossier
mv source destination

# --------------------------------------------------
# --------------- GESTION DES DROITS ---------------
# --------------------------------------------------

# Change les permissions d'un fichier ou dossier
# 777 : Donne tous les droits (lecture, écriture, exécution) à tout le monde
# u+x : Donne le droit d'exécution à l'utilisateur propriétaire
chmod 777 nom_du_fichier
chmod u+x nom_du_fichier

# Change le propriétaire d'un fichier ou dossier
chown utilisateur:utilisateur nom_du_fichier

# Accède au compte root (attention aux risques !)
sudo su

# Exécute une commande en tant qu'administrateur
sudo commande

# --------------------------------------------------
# --------------- GESTION DES PROCESSUS -------------
# --------------------------------------------------

# Liste les processus en cours
top

# Liste les processus de l'utilisateur actuel
ps

# Tue un processus par son PID
kill PID

# Tue un processus par son nom
killall nom_du_processus

# --------------------------------------------------
# --------------- ÉDITION DE FICHIERS ---------------
# --------------------------------------------------

# Ouvre le fichier en mode édition avec nano
nano nom_du_fichier

# Pour quitter nano :
# - Ctrl + X : Quitter
# - Y : Sauvegarder
# - N : Ne pas sauvegarder

# --------------------------------------------------
# ---------------- RECHERCHE D'INFO ----------------
# --------------------------------------------------

# Affiche le manuel d'une commande
man nom_de_la_commande

# Donne une description rapide d'une commande
whatis nom_de_la_commande

# Recherche des fichiers et dossiers
find /chemin/vers/dossier -name "*.txt"

# Recherche d'un mot ou motif dans un fichier
grep "motif" nom_du_fichier

# Exemple : Trouver toutes les lignes contenant "erreur" dans fichier.log
grep "erreur" fichier.log

# Recherche les fichiers contenant un motif
grep -r "motif" /chemin/vers/dossier

# Whois d'un nom de domaine
whois exemple.com

# --------------------------------------------------
# ------------------- REDIRECTION -------------------
# --------------------------------------------------

# Redirection de la sortie standard vers un fichier
commande > fichier.txt

# Ajout à un fichier existant
commande >> fichier.txt

# Redirection de la sortie d'erreur vers un fichier
commande 2> fichier_erreurs.txt

# Redirection de la sortie standard et des erreurs
commande > fichier.txt 2>&1

# Utiliser le contenu d'un fichier comme entrée
commande < fichier.txt

# Pipe : redirige la sortie d'une commande comme entrée d'une autre
commande1 | commande2

# Exemple : Trouver les fichiers ".txt" et chercher "erreur" dans leur contenu
find . -name "*.txt" | xargs grep "erreur"

# --------------------------------------------------
# -------------------- VARIABLES --------------------
# --------------------------------------------------

# Définir une variable
ma_variable="Bonjour le monde"

# Afficher le contenu d'une variable
echo $ma_variable

# Lire l'entrée de l'utilisateur
read nom_utilisateur

# Afficher le message avec le nom utilisateur
echo "Bonjour, $nom_utilisateur!"

# --------------------------------------------------
# -------------------- BOUCLES ---------------------
# --------------------------------------------------

# Boucle for
for i in {1..5}; do
  echo "Nombre : $i"
done

# Boucle while
compteur=1
while [ $compteur -le 5 ]; do
  echo "Nombre : $compteur"
  compteur=$((compteur+1))
done

# Boucle until
compteur=1
until [ $compteur -gt 5 ]; do
  echo "Nombre : $compteur"
  compteur=$((compteur+1))
done

# --------------------------------------------------
# -------------------- CONDITIONS -------------------
# --------------------------------------------------

# Condition if
if [ $variable -eq 5 ]; then
  echo "La variable vaut 5"
else
  echo "La variable ne vaut pas 5"
fi

# Condition case
case $variable in
  "valeur1")
    echo "Valeur 1"
    ;;
  "valeur2")
    echo "Valeur 2"
    ;;
  *)
    echo "Valeur inconnue"
    ;;
esac

# --------------------------------------------------
# ------------------- FONCTIONS ---------------------
# --------------------------------------------------

# Définir une fonction
ma_fonction() {
  echo "Bonjour depuis la fonction !"
}

# Appeler la fonction
ma_fonction

# Fonction avec arguments
ma_fonction() {
  echo "Bonjour, $1 !"
}

# Appeler la fonction avec un argument
ma_fonction "Utilisateur"

# --------------------------------------------------
# ---------------------- BONUS ----------------------
# --------------------------------------------------

# Détection du type de fichier
file nom_du_fichier

# Voir l'espace disque utilisé
df -h

# Voir l'espace disque utilisé dans le répertoire courant
du -sh *

# Voir la mémoire utilisée
free -h

# Redémarre la machine (ATTENTION !)
sudo reboot

# Arrête la machine (ATTENTION !)
sudo shutdown -h now

# Envoyer un ping à une adresse
ping -c 4 google.com

# Historique des commandes
history

# Exécute la commande n° 42 de l'historique
!42

# Clear : efface l'affichage du terminal
clear

# Voir l'adresse IP de la machine
ip a

# Voir les interfaces réseau disponibles
ifconfig

# Teste la connectivité vers un port
nc -zv google.com 80
