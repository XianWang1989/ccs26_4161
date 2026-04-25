
import requests
from bs4 import BeautifulSoup
import os

# Function to download image
def download_image(img_url, folder='images'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(img_url)
    if response.status_code == 200:
        img_name = os.path.join(folder, img_url.split('/')[-1])
        with open(img_name, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded image: {img_name}')

# Function to crawl pages and extract user data
def crawl_user_data(base_url, max_id):
    for user_id in range(1, max_id + 1):
        url = f"{base_url}?id={user_id}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page {user_id}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        users = soup.find_all('a')

        for user in users:
            img_tag = user.find('img')
            if img_tag and img_tag['src']:
                img_url = img_tag['src']
                download_image(img_url)

            name_tag = user.find_next('h1', class_='username')
            title_tag = user.find_next('p', class_='headline')

            if name_tag and title_tag:
                name = name_tag.text.strip()
                title = title_tag.text.strip()
                print(f"Name: {name}, Title: {title}")

# Usage
base_url = 'https://example.com'
max_id = 100
crawl_user_data(base_url, max_id)
