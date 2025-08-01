import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tripadvisor(location_id, max_reviews=1000):
    base_url = f"https://www.tripadvisor.com/Attraction_Review-g{location_id}"
    reviews = []