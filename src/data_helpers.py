import pandas as pd
import json

# Extrait les données json dans un DataFrame
def extract_data(path: str):
    data_file = open(path)
    name_file = path.split("/")[- 1]

    print(f"Extraction du fichier : {name_file}")

    data = [json.loads(line) for line in data_file]
    df = pd.DataFrame(data)

    return df

# Affiche la taille du jeu de données
def displayDataShape(message, data):
    shape = data.shape
    print(f"{message} : {shape[0]} lignes et {shape[1]} colonnes\n")

