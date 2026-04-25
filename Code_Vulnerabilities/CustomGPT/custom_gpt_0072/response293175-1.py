
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Base URL
base_url = 'https://example.com?id='

for page_id in range(1, 101):
    url = f"{base_url}{page_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user containers (modify the selector as needed)
    users = soup.find_all('div', class_='user-container')  # Adjust this line

    for user in users:
        # Scrape user photo
        img_tag = user.find('img')
        user_photo_url = img_tag['src'] if img_tag else None
        if user_photo_url:
            img_response = requests.get(user_photo_url)
            img_name = os.path.join('user_images', user_photo_url.split('/')[-1])
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

        # Scrape username and title
        username = user.find('h1', class_='username').get_text(strip=True) if user.find('h1', class_='username') else 'N/A'
        title = user.find('p', class_='headline').get_text(strip=True) if user.find('p', class_='headline') else 'N/A'

        # Output to another site or print
        print(f"User: {username}, Title: {title}, Photo saved as: {img_name if user_photo_url else 'No photo'}")
