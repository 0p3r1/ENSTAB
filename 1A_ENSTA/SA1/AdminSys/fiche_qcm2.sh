# --------------------------------------------------
# -------------------- ADMIN SYS -------------------
# ---------------------- SHELL ---------------------
# --------------------------------------------------

# --------------------------------------------------
# ---------------------- GREP ----------------------
# --------------------------------------------------


# Recherche d'un motif en ignorant la casse (majuscules/minuscules)
grep -i "motif" fichier.txt

# Recherche d'un motif exact, sans correspondre à une partie d'un mot
grep -w "motif" fichier.txt

# Recherche avec des caractères spéciaux (exemple pour un point qui n'est pas un joker)
grep "\." fichier.txt

# Recherche d'un motif en début de ligne
grep "^motif" fichier.txt

# Recherche d'un motif en fin de ligne
grep "motif$" fichier.txt

# Recherche d'un motif au début d'une ligne et à la fin de la ligne
grep "^motif$" fichier.txt

# Recherche d'un motif avec des caractères spéciaux, comme une barre oblique
grep "\/" fichier.txt

# Recherche avec des expressions régulières (par exemple, chercher "motif1" ou "motif2")
grep -E "motif1|motif2" fichier.txt

# Recherche dans les fichiers récursivement et affiche le nom du fichier avant chaque ligne trouvée
grep -r "motif" /chemin/vers/dossier

# Affiche les lignes ne contenant PAS un motif
grep -v "motif" fichier.txt

# Affiche le nombre de lignes contenant un motif
grep -c "motif" fichier.txt

# Recherche les lignes qui contiennent n'importe quel caractère sauf ceux définis
grep -v "[a-z]" fichier.txt  # Toutes les lignes sans lettres minuscules

# Recherche avec une correspondance d'un ou plusieurs caractères
grep -E "motif{2,}" fichier.txt  # Au moins 2 occurrences de "motif"

# Recherche d'un motif exact dans plusieurs fichiers
grep "motif" *.txt

# --------------------------------------------------
# ---------------------- AWK -----------------------
# --------------------------------------------------

# Affiche une colonne spécifique (exemple, la deuxième colonne)
awk '{print $2}' fichier.txt

# Filtre les lignes selon une condition (exemple, la première colonne est égale à "valeur")
awk '$1 == "valeur" {print}' fichier.txt

# Filtre et affiche des colonnes avec une condition sur une autre colonne
awk '$3 > 100 {print $1, $2, $3}' fichier.txt  # Si la 3e colonne est supérieure à 100

# Calcul de la somme d'une colonne
awk '{sum+=$1} END {print "Somme =", sum}' fichier.txt

# Modifier le séparateur de colonnes (par exemple, avec un autre délimiteur comme une virgule)
awk -F "," '{print $1, $2}' fichier.csv

# Utiliser une fonction avec AWK (exemple pour capitaliser le texte)
awk '{print toupper($1)}' fichier.txt  # Convertir en majuscule la première colonne

# Utilisation d'AWK avec plusieurs conditions sur les colonnes
awk '$1 == "nom" && $3 > 10 {print $1, $2, $3}' fichier.txt

# --------------------------------------------------
# ---------------------- SED -----------------------
# --------------------------------------------------

# Remplace un motif par un autre dans tout le fichier
sed 's/motif/nouveau_motif/g' fichier.txt

# Remplace un motif seulement pour la première occurrence sur chaque ligne
sed 's/motif/nouveau_motif/' fichier.txt

# Remplace un motif sans tenir compte de la casse
sed 's/motif/nouveau_motif/Ig' fichier.txt

# Remplace un motif seulement dans une plage de lignes (par exemple de la ligne 10 à 20)
sed '10,20s/motif/nouveau_motif/g' fichier.txt

# Supprime les lignes contenant un motif
sed '/motif/d' fichier.txt

# Ajoute une ligne après chaque ligne correspondant à un motif
sed '/motif/a Nouvelle ligne' fichier.txt

# Remplace un motif sur une ligne spécifique (par exemple, la ligne 5)
sed '5s/motif/nouveau_motif/' fichier.txt

# Afficher et modifier en même temps avec sed
sed -n 's/motif/nouveau_motif/p' fichier.txt  # Affiche uniquement les lignes modifiées

# Utilisation de sed avec des expressions régulières avancées
sed -E 's/(motif[0-9]+)/nouveau_motif/g' fichier.txt  # Remplacer les motifs suivis de chiffres

# --------------------------------------------------
# ----------------------- VI -----------------------
# --------------------------------------------------

# Ouvre le fichier en mode édition avec vi
vi fichier.txt

# Mode insertion : Appuyez sur 'i'
# Supprimer caractère : Appuyez sur 'x'
# Enregistrer et quitter : Appuyez sur ':wq'
