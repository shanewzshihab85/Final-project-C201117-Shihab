import requests

# Base URL for the API
API_BASE_URL = "http://localhost:8011"

# Function to get a list of news items with optional pagination
def get_news_list(skip=0, limit=10):
    response = requests.get(f"{API_BASE_URL}/news/?skip={skip}&limit={limit}")
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to get a specific news item by its ID
def get_news_by_id(news_id):
    response = requests.get(f"{API_BASE_URL}/news/{news_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to scrape news articles from a list of URLs
def scrape_news(urls):
    response = requests.post(f"{API_BASE_URL}/news/scrape/", json=urls)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to get a summary for a specific news item by its ID
def get_summary(news_id):
    summary_data = {"news_id": news_id}
    response = requests.post(f"{API_BASE_URL}/summaries/", json=summary_data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get a summary by its specific ID
def get_summary_by_id(summary_id):
    response = requests.get(f"{API_BASE_URL}/summaries/{summary_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
