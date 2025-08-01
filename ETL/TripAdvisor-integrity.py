import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tripadvisor(location_id, max_reviews=1000):
    base_url = f"https://www.tripadvisor.com/Attraction_Review-g{location_id}"
    reviews = []

    for i in range(0, max_reviews, 10):
        url = f"{base_url}-Reviews-or{i}-Attraction_Name.html"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for review in soup.find_all('div', class_='review-container'):
            text = review.find('q', class_='review-text').text
            rating = review.find('span', class_='ui_bubble_rating')['class'][1].split('_')[1]
            reviews.append({'text': text, 'rating': int(rating)/10})
    
    return pd.DataFrame(reviews)