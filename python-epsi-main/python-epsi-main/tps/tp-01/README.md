# Correction du TP1

## Rappel des consignes: 


Lire un fichier csv et le stocker en mémoire. Puis ensuite proposer un prompt à l'utilisateur
permettant de :

* Chercher une ville ("get city $city") --> Retourne la ville en entier
* Lister les villes présente dans un département ("get department $department")
* Ajouter une nouvelle ville (add $city,$department,$country,$population)
* Ecrire le contenu de la mémoire dans le fichier db.csv (flush)
* Supprimer une ville ("delete $city")
* Supprimer un departement ("delete $department")

L'affichage se fait au format csv.

## Etapes

* Lecture du fichier
* Création de la classe City, permettant de stocker les données relatives à une ville
* Création de la classe DB, prenant en paramètre une liste de City, et permettant de répondre à l'ensemble des fonctionnalités demandées.
  * On veille à indexer les villes dans un dictionnaire, afin de ne pas avoir à relire le fichier à chaque requête.
  * On indexe ensuite les villes par département, de sorte de ne pas avoir à itérer sur toutes les villes.
  * Pour la suppression de "département", il est attendu que l'on supprime toutes les villes liées à un département. Vu que l'on a déjà une fonctionnalité de suppression de ville, autant la réutiliser afin de ne pas dupliquer du code inutilement.
* Création du parseur