
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = 'http://example.com?id='

# Directory to save images
image_dir = 'user_images'
os.makedirs(image_dir, exist_ok=True)

# Loop through page IDs
for page_id in range(1, 101):
    # Request the page
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user elements on the page
    users = soup.find_all('a', href=True)

    for user in users:
        # Get user photo, name, and title
        img_tag = user.find('img')
        if img_tag:
            img_url = img_tag['src']
            img_name = os.path.join(image_dir, os.path.basename(img_url))
            # Download the image
            img_response = requests.get(img_url)
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

        username = user.find_next('h1', class_='username')
        headline = user.find_next('p', class_='headline')

        if username and headline:
            print(f"User: {username.text.strip()}, Title: {headline.text.strip()}")

# Output the retrieved data as needed
