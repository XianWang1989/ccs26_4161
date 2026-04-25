
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('images', exist_ok=True)

# Base URL
base_url = 'http://example.com?id={}'

for page_id in range(1, 101):  # Loop through pages 1 to 100
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    users = soup.find_all('a')  # Adjust to target specific user links

    for user in users:
        img_tag = user.find('img')
        if img_tag and img_tag.get('src'):
            img_url = img_tag['src']
            name = user.find('h1', class_='username').text
            title = user.find('p', class_='headline').text

            # Download user photo
            img_response = requests.get(img_url)
            with open(f'images/{name}.jpg', 'wb') as img_file:
                img_file.write(img_response.content)

            # Output user information
            print(f'Name: {name}, Title: {title}, Image saved as: {name}.jpg')
