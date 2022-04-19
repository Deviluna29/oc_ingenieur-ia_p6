import pandas as pd
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

# Affichage un nuage des mots les plus fréquents dans le data
def display_wordcloud(data, max_words):
    extract = []
    for row in data:
        extract+= row

    extract = " ".join(extract)

    wordcloud = WordCloud(background_color = 'white', max_words = max_words, stopwords = []).generate(extract)
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# Affiche un histogramme des mots les plus courants
def display_word_freq_hist(freq, number):

    freq_list = tuple(zip(*freq.most_common(number)))
    most_freq = pd.Series(freq_list[1], freq_list[0])

    plt.figure(figsize=(16, 10))
    most_freq.plot.bar()
    plt.title(f'Top {number} des mots les plus fréquents dans le corpus')
    plt.xlabel('Mots')
    plt.ylabel('Fréquence')
    plt.show()


