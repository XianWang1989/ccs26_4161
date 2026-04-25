
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "https://example.com?id="

# Create directory for images
os.makedirs("user_images", exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user elements
    users = soup.find_all('a', href=True)

    for user in users:
        user_image = user.find('img')['src']
        username = user.find_next('h1', class_='username').text
        headline = user.find_next('p', class_='headline').text

        # Download the image
        image_response = requests.get(user_image)
        image_filename = os.path.join("user_images", f"{username}.jpg")

        with open(image_filename, 'wb') as img_file:
            img_file.write(image_response.content)

        # Output the user data
        print(f"Name: {username}, Title: {headline}, Image saved as: {image_filename}")
