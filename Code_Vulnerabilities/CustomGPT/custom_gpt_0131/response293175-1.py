
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
base_url = 'https://example.com?id='

# Function to scrape user data from a page
def scrape_users(page_number):
    url = f"{base_url}{page_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        users = []

        # Find all user containers in the page
        for user_container in soup.find_all('div', class_='user-container'):  # Adjust selector as necessary
            user_photo = user_container.find('img')['src']
            username = user_container.find('h1', class_='username').text
            headline = user_container.find('p', class_='headline').text

            users.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

        return users
    else:
        print(f"Failed to retrieve page {page_number}, status code: {response.status_code}")
        return []

# Scrape all pages from 1 to 100
all_users = []
for i in range(1, 101):
    users_on_page = scrape_users(i)
    all_users.extend(users_on_page)

# Output scraped data (for example purposes, we will just print)
for user in all_users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")

# You can then output this content to another site or use it as needed
