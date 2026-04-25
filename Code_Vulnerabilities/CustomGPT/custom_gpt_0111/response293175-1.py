
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to store the downloaded images
os.makedirs('user_images', exist_ok=True)

# Function to download an image
def download_image(url, username):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'user_images/{username}.jpg', 'wb') as f:
            f.write(response.content)

# Main crawler function
def crawl_users(base_url, pages):
    for page_id in range(1, pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            users = soup.find_all('a')  # Modify this to the right tag if necessary

            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    print(f"User: {username}, Title: {headline}, Photo URL: {user_photo}")

                    # Download the user photo
                    download_image(user_photo, username)

# Base URL of the site to crawl
base_url = 'http://example.com'
# Specify how many pages to crawl
crawl_users(base_url, 100)
