
import requests
from bs4 import BeautifulSoup
import os

# Create a directory for downloaded images
os.makedirs('user_images', exist_ok=True)

# Base URL of the site
base_url = 'http://example.com?id={}'

# Loop through pages 1 to 100
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user containers (adjust the selector as needed)
    users = soup.find_all('a', href=True)

    for user in users:
        img_tag = user.find('img')
        if img_tag:
            image_url = img_tag['src']
            user_name = user.find_next('h1', class_='username').text
            user_title = user.find_next('p', class_='headline').text

            # Download the image
            img_response = requests.get(image_url)
            img_name = os.path.join('user_images', f"{user_name}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output the user's data
            print(f'Name: {user_name}, Title: {user_title}, Image: {img_name}')

print('Crawling completed!')
