
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save the images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Base URL
base_url = 'http://example.com?id={}'

# Loop through the pages
for page_id in range(1, 101):
    url = base_url.format(page_id)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user blocks on the page
    user_blocks = soup.find_all('a', href=True)

    for user_block in user_blocks:
        user_photo = user_block.find('img')['src']
        username = user_block.find_next('h1', class_='username').text
        headline = user_block.find_next('p', class_='headline').text

        # Save the image
        img_response = requests.get(user_photo)
        img_name = f"user_images/{username}.jpg"
        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)

        # Output user info
        print(f'User: {username}, Title: {headline}, Image saved as: {img_name}')
