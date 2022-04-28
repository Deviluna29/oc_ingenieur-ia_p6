## Configuration

Renommer le fichier .env_sample en .env et renseigner les valeurs des variables d'environnement (pour l'API yelp)

## Résultats des Notebooks sous format HTML

Les résultats des notebooks, en HTML avec les graphes interactifs :

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p6/P06_02_notebook_analyse>HTML Notebook analyse et merge</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p6/P06_03_notebook_nlp.html>HTML Notebook NLP</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p6/P06_04_notebook_cv.html>HTML Notebook Computer Vison</a>

## Installation de l'environnement virtuel

Créer l'environnement à partir du fichier yaml
```bash
conda env create -f environment.yml
```

Activer l'environnement
```bash
conda activate projet_ml
```

## Téléchargement du jeu de données

Récupérer les jeux de données <a href = https://www.yelp.com/dataset>à cette adresse</a>

Dezipper le fichier dans le dossier "data/"

Il doit y avoir ces 2 dossiers :

yelp_dataset/
yelp_photos/

## Utilisation des notebooks

Lancer les scripts suivants dans l'ordre :

- le fichier "P06_01_api.py" pour collecter certaines données via l'api, ce script va crée un fichier "bad_reviews_from_api.csv" à la racine

- le notebook "P06_02_notebook_analyse.ipynb" qui sert au merge des données, celui ci va créer un fichier "bad_reviews.csv" à la racine.


Une fois ces 2 fichiers créés, les autres notebooks peuvent être utilisés
