
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Base URL of the site to crawl
base_url = 'http://example.com?id='

# Loop through the pages
for i in range(1, 101):
    url = f'{base_url}{i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find user entries on the page
    users = soup.find_all('a')  # Adjust selector as necessary

    for user in users:
        # Extract user photo, name, and title
        img_tag = user.find('img')
        username_tag = user.find_next('h1', class_='username')
        headline_tag = user.find_next('p', class_='headline')

        if img_tag and username_tag and headline_tag:
            user_photo_url = img_tag['src']
            username = username_tag.text
            headline = headline_tag.text

            # Download the image
            img_response = requests.get(user_photo_url)
            img_filename = os.path.join('user_images', f"{username}.jpg")

            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output the user data
            print(f'Username: {username}, Title: {headline}, Image saved as: {img_filename}')
