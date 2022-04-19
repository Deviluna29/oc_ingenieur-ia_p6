from dotenv import load_dotenv
import requests
import os
import pandas as pd

load_dotenv()
# Récupérer les valeurs des variables d'environnement pour l'authentification
api_key = "Bearer " + os.getenv("YELP_API_KEY")

endpoint = "https://api.yelp.com/v3/businesses"
path_search = "/search"
path_reviews = "/reviews"

cities = ['NYC', 'CA', 'FL', 'TX']
businesses_id = []
reviews = []

# Requête pour récupérer les id de restaurants
def businesses_request():

    constructed_url = endpoint + path_search
    headers = {'Authorization': api_key}

    for city in cities:

        query = {'categories': 'restaurants', 'location': city, 'limit': '50'}

        print(f"Request businesses for city {city}")
        response = requests.get(constructed_url, params=query, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for business in data['businesses']:
                if business['id'] not in businesses_id:
                    businesses_id.append(business['id'])

        else:
            print(f"An error occured : {response.content}")

# Requête pour récupérer les reviews des restaurants
def reviews_request():

    headers = {'Authorization': api_key}
    i = 1

    for id in businesses_id:

        constructed_url = endpoint + f"/{id}" + path_reviews

        print(f"Request reviews n°{i} for business {id}")
        response = requests.get(constructed_url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for review in data['reviews']:
                # On ne garde que les mauvaises reviews
                if review['rating'] <= 1:
                    reviews.append([id, 'Restaurants', review['rating'], review['text'].replace('\n', ' ')])

        else:
            print(f"An error occured : {response.content}")

        i += 1

def main():
    businesses_request()

    if len(businesses_id) == 200:
        reviews_request()
    else:
        return print(f"An error occured while completing Businesses id list, length : {len(businesses_id)}")

    if len(reviews) > 0:
        df = pd.DataFrame(data=reviews, columns=['business_id', 'categories', 'stars', 'text'])
        df.to_csv('bad_reviews_from_api.csv', index=False)
        print(f"{df.shape[0]} bad reviews saved in file bad_reviews_from_api.csv")
    else:
        return print(f"An error occured while completing Reviews list, length : {len(reviews)}")

if __name__ == "__main__":
    main()

