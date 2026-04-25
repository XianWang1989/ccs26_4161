
import requests
from bs4 import BeautifulSoup
import os

# Function to download images
def download_image(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        image_name = url.split("/")[-1]
        with open(os.path.join(folder, image_name), 'wb') as f:
            f.write(response.content)

# Base URL
base_url = "http://example.com?id={}"
user_data = []

# Create a folder for downloaded images
os.makedirs('user_images', exist_ok=True)

# Crawl pages
for page_id in range(1, 101):  # Looping through pages 1 to 100
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user blocks (assuming a div with class 'user')
        users = soup.find_all('div', class_='user')  # Adjust based on actual HTML structure

        for user in users:
            photo_tag = user.find('img')
            name_tag = user.find('h1', class_='username')
            title_tag = user.find('p', class_='headline')

            if photo_tag and name_tag and title_tag:
                user_photo = photo_tag['src']
                username = name_tag.text.strip()
                headline = title_tag.text.strip()

                # Save photo URL and user data
                user_data.append({'name': username, 'title': headline, 'photo': user_photo})

                # Download image
                download_image(user_photo, 'user_images')

# Output the collected user data
for user in user_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
