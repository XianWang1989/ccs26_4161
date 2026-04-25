
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "https://example.com?id="

# Directory to save images
os.makedirs("user_images", exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries on the page
    users = soup.find_all('a', href=True)

    for user in users:
        user_name = user.find_next('h1', class_='username').text.strip()
        user_title = user.find_next('p', class_='headline').text.strip()
        image_url = user.find('img')['src']

        # Download the image
        img_response = requests.get(image_url)
        img_path = os.path.join("user_images", f"{user_name.replace(' ', '_')}.jpg")
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)

        # Output the user information
        print(f"Downloaded {user_name}: {user_title} - {img_path}")

print("Crawling completed!")
