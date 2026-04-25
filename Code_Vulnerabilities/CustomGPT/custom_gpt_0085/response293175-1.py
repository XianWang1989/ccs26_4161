
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = 'https://example.com?id={}'

# Directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    if response.status_code != 200:
        print(f"Failed to retrieve page {page_id}")
        continue

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries
    users = soup.find_all('a', href=True)

    for user in users:
        img_tag = user.find('img')
        if img_tag:
            user_photo = img_tag['src']
            # Download the image
            img_response = requests.get(user_photo)
            img_filename = os.path.join('user_images', os.path.basename(user_photo))
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)

        username = user.find_next('h1', class_='username').text.strip()
        headline = user.find_next('p', class_='headline').text.strip()

        # Output the user data (here we're just printing it)
        print(f'User: {username}, Title: {headline}, Photo: {img_filename}')

        # Here you can format this data for output on another site
