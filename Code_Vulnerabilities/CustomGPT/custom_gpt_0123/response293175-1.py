
import requests
from bs4 import BeautifulSoup
import os

# Base URL and target folder for images
base_url = "http://example.com?id={}"
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# Iterate through the page IDs
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries
    users = soup.find_all('a', href=True)

    for user in users:
        img_tag = user.find('img')
        if img_tag:
            user_photo = img_tag['src']
            username = user.find_next('h1', class_='username').text.strip()
            headline = user.find_next('p', class_='headline').text.strip()

            # Download the image
            img_response = requests.get(user_photo)
            img_name = os.path.join(output_folder, os.path.basename(user_photo))
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output user data
            print(f"User: {username}, Title: {headline}, Photo: {img_name}")
