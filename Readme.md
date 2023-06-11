# SQL Compare - v1
==================

Auteur : Fabien Cador

Email : fabiencador (at) gmail.com

Sommaire
--------

- [A propos de SQL Compare](#a-propos-de-sql-compare)
- [Bibliothèques utilisées](#bibliotheques-utilisees)
- [Utilisation](#utilisation)
- [A venir](#a-venir)

## A propos de SQL Compare

SQL Compare est un projet né de 2 besoins :

- Celui de comparer régulièrement, sur un projet, un schéma de base de données local à celui en production.
- Et celui de mettre en pratique des notions de Python fraîchement acquises.

Ce script permet de faire une comparaison basique de 2 bases de données et de rapporter les différences entre une base A (par exemple locale et comprenant de potentiels nouveaux champs) et une base B (par exemple en production).

## Bibliothèques utilisées

- sqlparse-0.4.4
- tkinter

## Utilisation

Vous pouvez utiliser SQL Compare de 2 façons :

**1ère solution** - Si vous choisissez d'exécuter le script non compilé :

- Ouvrez une fenêtre d'invite de commande.
- Assurez-vous d'avoir Python installé sur votre ordinateur en exécutant `python --version`.
- Accédez au script `cd chemin/vers/le/script/`.
- Exécutez le script `python sql_compare.py`.

**2ème solution** - Si vous disposez du fichier exécutable et que vous choisissez de passer par celui-ci :

- Exécutez sql_compare.exe.

Une fois le script lancé :

- La première fenêtre vous demandera de choisir l'emplacement du fichier *.sql source (exemple : bdd locale).
- Choisissez l'emplacement du fichier *.sql de destination (exemple : bdd de production).
- Choisissez l'emplacement où le fichier de différence *.csv sera enregistré.
- Consultez les différences dans le fichier *.csv.

## A venir

- Possibilité d'avoir la requête SQL permettant de rétablir les différences dans le fichier *.csv.
- Factorisation des tests effectués pour obtenir les différences.
- Localisation.
