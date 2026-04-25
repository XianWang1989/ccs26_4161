
import requests
from bs4 import BeautifulSoup

# Function to scrape user data
def scrape_user_data(base_url, pages):
    user_data = []

    for page_id in range(1, pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a', href=True)

            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    user_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline
                    })
        else:
            print(f"Failed to retrieve data from page {page_id}")

    return user_data

# Base URL of the site you want to crawl
base_url = 'https://example.com'
# Total number of pages to crawl
total_pages = 100

# Get the user data
users = scrape_user_data(base_url, total_pages)

# Output the user data
for user in users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
