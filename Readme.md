SQL Compare - v1
=====

Auteur : Fabien Cador
Email : <fabiencador@gmail.com>

A propos de SQL Compare
-----

SQL Compare est un projet né de 2 besoins:

* Celui de régulièrement avoir à comparer, sur un projet, un schéma de base de données local à celui en production.
* Et de celui de mettre en pratique des notions de Python fraichement acquises

Ce script permet de faire une comparaison basique de 2 bases de données et de reporter les différences entre une base A (par exemple locale et comprenant de potentiels nouveaux champs) et une base B (par exemple en production)

Bibliothèques utilisées
-----

* sqlparse-0.4.4
* tkinter

Utilisation
-----

* Ouvrir l'executable.
* La première fenêtre vous demandera de choisir l'emplacement du fichier *.sql source (exemple : bdd locale)
* Choisir l'emplacement du fichier *.sql de destination (exemple : bdd de production)
* Choisir l'emplacement où le fichier de différence *.csv s'enregistrera.
* Consulter les différences dans le fichier *.csv

A venir
-----

* Possibilité d'avoir la requête SQL permettant de rétablir les différences dans le fichier *.csv
* Factorisation des tests effectuées pour obtenir les différences