
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to store images
if not os.path.exists('user_photos'):
    os.makedirs('user_photos')

# Base URL
base_url = 'http://example.com?id='

# Loop through the pages
for page_id in range(1, 101):  # From id=1 to id=100
    url = f'{base_url}{page_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find user entries
    users = soup.find_all('a', href=True)  # Find all anchor tags
    for user in users:
        img_tag = user.find('img')
        if img_tag and 'userphoto' in img_tag['src']:
            user_photo_url = img_tag['src']
            user_name = user.find_next('h1', class_='username').text
            user_title = user.find_next('p', class_='headline').text

            # Print user data
            print(f'Name: {user_name}, Title: {user_title}, Photo URL: {user_photo_url}')

            # Download the image
            img_response = requests.get(user_photo_url)
            img_name = os.path.join('user_photos', user_photo_url.split('/')[-1])
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

