import requests
import random

BASE_URL = "https://randomuser.me/api/?nat=gb"
PARTIES = ["management party", "Saviour party", "Tech Army Party"]

random.seed(21)

def generate_candidate_data(candidate_number: int, total_parties: int) -> dict: 
    """
    Method used to generate fake candidate data

    Input: Candidate number (INT)
           Total parties (INT)
    Output: Candidate data (DICT)

    """
    response = requests.get(BASE_URL + '&gender=' + ('female' if candidate_number % 2 == 1 else 'male'))
    if response.status_code == 200:
        user_data = response.json()['results'][0]


        return {
            "candidate_id": user_data['login']['uuid'],
            "candidate_name": f"{user_data['name']['first']} {user_data['name']['last']}",
            "party_affiliation": PARTIES[candidate_number % total_parties],
            "biography": "A brief bio of the candidate.",
            "campaign_platform": "Key campaign promises or platform.",
            "photo_url": user_data['picture']['large']
        }
    else:
        return "Error fetching data"