
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "http://example.com?id="

# Create a directory for downloaded images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Loop through page IDs
for page_id in range(1, 101):
    response = requests.get(f"{base_url}{page_id}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo_url = user.find('img')['src']
            username = user.find_next('h1', class_='username').text.strip()
            headline = user.find_next('p', class_='headline').text.strip()

            # Download the user photo
            photo_response = requests.get(user_photo_url)
            if photo_response.status_code == 200:
                photo_filename = os.path.join('user_images', f"{username}.jpg")
                with open(photo_filename, 'wb') as f:
                    f.write(photo_response.content)

            # Output the user data (This could be modified to output to another site)
            print(f"User: {username}, Title: {headline}, Photo: {photo_filename}")

    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")
