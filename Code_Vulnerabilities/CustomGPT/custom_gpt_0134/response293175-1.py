
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = "http://example.com?id="

# Directory to save downloaded images
image_dir = "user_images"
os.makedirs(image_dir, exist_ok=True)

for page_id in range(1, 101):  # Loop through pages 1 to 100
    # Fetch each page
    response = requests.get(base_url + str(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user elements on the page
        user_tags = soup.find_all('a', href=True)

        for user_tag in user_tags:
            # Extract user photo, name and title
            user_photo = user_tag.find('img')['src']
            username = user_tag.find_next('h1', class_='username').text
            title = user_tag.find_next('p', class_='headline').text

            # Print or store the information
            print(f"Name: {username}, Title: {title}, Photo URL: {user_photo}")

            # Download the photo
            img_response = requests.get(user_photo)
            if img_response.status_code == 200:
                # Create a local image file
                with open(os.path.join(image_dir, f"{username}.jpg"), 'wb') as img_file:
                    img_file.write(img_response.content)

    else:
        print(f"Failed to retrieve page {page_id}")

print("Crawling completed.")
