
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = "https://example.com?id={}"

# Directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the range of pages
for page_id in range(1, 101):
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all users on the page (assuming they are in a specific container)
        users = soup.find_all('div', class_='user-container')  # Update with correct class

        for user in users:
            # Extract user photo, name, and title
            user_photo = user.find('img')['src']
            username = user.find('h1', class_='username').text
            headline = user.find('p', class_='headline').text

            # Download image
            image_response = requests.get(user_photo)
            image_path = os.path.join('user_images', f"{username}.jpg")
            with open(image_path, 'wb') as img_file:
                img_file.write(image_response.content)

            # Output user details
            print(f"Downloaded {username}'s image and data:")
            print(f"Name: {username}, Title: {headline}, Image saved to: {image_path}")
    else:
        print(f"Failed to retrieve page {page_id}, Status code: {response.status_code}")
