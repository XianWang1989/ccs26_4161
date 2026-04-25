
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Base URL
base_url = 'https://example.com?id={}'

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries on the page
    users = soup.find_all('a', href=True)

    for user in users:
        # Extract user photo, name, and title
        img_tag = user.find('img')
        if img_tag:
            photo_url = img_tag['src']
            user_name = user.find_next('h1', class_='username').text
            user_title = user.find_next('p', class_='headline').text

            # Download the image
            img_response = requests.get(photo_url)
            img_name = os.path.join('user_images', f"{user_name}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output user data
            print(f"Name: {user_name}, Title: {user_title}, Photo saved as: {img_name}")

print("Crawling complete!")
