
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
BASE_URL = "http://example.com?id={}"

# Directory to save images
IMAGE_DIR = "downloaded_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Function to download images
def download_image(img_url, user_name):
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(os.path.join(IMAGE_DIR, f"{user_name}.jpg"), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded {user_name}'s image.")
        else:
            print(f"Failed to download image: {img_url}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Loop through pages
for page_id in range(1, 101):
    response = requests.get(BASE_URL.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a')

        for user in users:
            img_tag = user.find('img')
            if img_tag and 'src' in img_tag.attrs:
                user_photo = img_tag['src']
                user_name = user.find_next('h1', class_='username').text.strip()
                user_title = user.find_next('p', class_='headline').text.strip()

                # Print the extracted data
                print(f"Name: {user_name}, Title: {user_title}, Photo URL: {user_photo}")

                # Download the user photo
                download_image(user_photo, user_name)

    else:
        print(f"Failed to retrieve page {page_id}. Status code: {response.status_code}")
