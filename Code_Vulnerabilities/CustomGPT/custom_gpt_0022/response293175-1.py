
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = 'http://example.com?id={}'

# Function to crawl pages
def crawl_and_save_data(start_id, end_id):
    user_data = []

    for page_id in range(start_id, end_id + 1):
        url = base_url.format(page_id)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find user elements
            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    img_url = img_tag['src']
                    name = user.find_next('h1', class_='username').text
                    title = user.find_next('p', class_='headline').text

                    # Download the image
                    download_image(img_url, name)

                    # Save user data
                    user_data.append({
                        'name': name,
                        'title': title,
                        'img_url': img_url
                    })

    return user_data

# Function to download images
def download_image(img_url, name):
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        img_name = f"{name}.jpg"
        with open(os.path.join('images', img_name), 'wb') as f:
            f.write(img_response.content)

# Create a directory for images
os.makedirs('images', exist_ok=True)

# Start crawling (for example, from id 1 to 100)
user_data = crawl_and_save_data(1, 100)

# Output collected data
for user in user_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Image: {user['img_url']}")
