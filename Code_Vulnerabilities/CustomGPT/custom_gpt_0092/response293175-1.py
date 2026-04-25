
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = "http://example.com?id={}"

# Directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user elements on the page
        users = soup.find_all('a', href=True)

        for user in users:
            img_tag = user.find('img')
            user_photo = img_tag['src'] if img_tag else None
            username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else "Unknown"
            headline = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else "No title"

            # Output user data
            print(f"Name: {username}, Title: {headline}, Photo URL: {user_photo}")

            # Download the user photo
            if user_photo:
                img_response = requests.get(user_photo)
                if img_response.status_code == 200:
                    img_name = os.path.join('user_images', os.path.basename(user_photo))
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)
                else:
                    print(f"Failed to download image: {user_photo}")
    else:
        print(f"Failed to retrieve page {page_id}")
