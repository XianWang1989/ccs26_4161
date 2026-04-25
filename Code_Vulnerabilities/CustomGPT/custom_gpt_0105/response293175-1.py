
import requests
from bs4 import BeautifulSoup
import os

# Create directory to save images
os.makedirs('user_images', exist_ok=True)

base_url = 'http://example.com?id='

# Iterate through the page IDs
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user elements on the page
    users = soup.find_all('a', href=True)

    for user in users:
        user_photo = user.find('img')['src']
        user_name = user.find_next('h1', class_='username').text
        user_title = user.find_next('p', class_='headline').text

        # Download the user photo
        img_response = requests.get(user_photo)
        img_name = os.path.join('user_images', os.path.basename(user_photo))

        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)

        # Output the user data
        print(f'Name: {user_name}, Title: {user_title}, Photo saved as: {img_name}')

print("Crawling completed!")
