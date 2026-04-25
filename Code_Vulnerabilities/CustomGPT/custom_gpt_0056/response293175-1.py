
import requests
from bs4 import BeautifulSoup

# Base URL for the site
base_url = "http://example.com?id={}"

# Function to crawl pages
def crawl_pages(num_pages):
    user_data = []

    for page in range(1, num_pages + 1):
        response = requests.get(base_url.format(page))

        if response.status_code != 200:
            print(f"Failed to retrieve page {page}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all users on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text.strip()
            headline = user.find_next('p', class_='headline').text.strip()

            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

    return user_data

# Function to output user data to another site (example placeholder)
def output_data(user_data):
    for user in user_data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")

# Crawl the first 100 pages
user_data = crawl_pages(100)

# Output the data
output_data(user_data)

