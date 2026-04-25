
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "https://example.com?id={}"

# Directory to save images
if not os.path.exists("user_photos"):
    os.makedirs("user_photos")

# Loop through the pages
for page_id in range(1, 101):
    # Make a request to the page
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user containers (adjust based on actual HTML structure)
        users = soup.find_all('div', class_='user-container')  # Adjust class name

        for user in users:
            # Extract user photo, name, and title
            photo_url = user.find('img')['src']
            name = user.find('h1', class_='username').text.strip()
            title = user.find('p', class_='headline').text.strip()

            # Print user data (or save to a database or file as needed)
            print(f'Name: {name}, Title: {title}, Photo URL: {photo_url}')

            # Download the photo
            img_response = requests.get(photo_url)
            if img_response.status_code == 200:
                img_path = os.path.join("user_photos", f"{name.replace(' ', '_')}.jpg")
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)

    else:
        print(f"Failed to retrieve page {page_id}")
