
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = 'http://example.com?id={}'

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the pages (from 1 to 100)
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    # Check the response status
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find each user entry
        users = soup.find_all('div', class_='user-entry')  # Adjust selector as needed

        for user in users:
            # Extract user photo, name, and title
            user_photo = user.find('img')['src']
            username = user.find('h1', class_='username').text
            title = user.find('p', class_='headline').text

            # Download the user photo
            photo_response = requests.get(user_photo)
            photo_path = os.path.join('user_images', f"{username}.jpg")
            with open(photo_path, 'wb') as f:
                f.write(photo_response.content)

            # Output user data
            print(f"User: {username}, Title: {title}, Photo saved as: {photo_path}")
    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")
