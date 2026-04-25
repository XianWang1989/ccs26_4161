
import requests
from bs4 import BeautifulSoup
import os

# The base URL of the site you want to crawl
base_url = 'http://example.com?id='

# Directory to save downloaded images
os.makedirs('user_images', exist_ok=True)

for page_id in range(1, 101):  # Loop through pages 1 to 100
    response = requests.get(base_url + str(page_id))

    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user sections (modify according to actual structure)
        users = soup.find_all('a', href=True)  # Assume each user is wrapped in an anchor tag

        for user in users:
            img_tag = user.find('img')  # Get the image tag

            if img_tag:
                user_photo_url = img_tag['src']  # Get the photo URL
                username = user.find_next('h1', class_='username').text.strip()  # User name
                headline = user.find_next('p', class_='headline').text.strip()  # User title

                # Download the user photo
                img_response = requests.get(user_photo_url)
                if img_response.status_code == 200:
                    img_name = os.path.join('user_images', f"{username}.jpg")
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)

                print(f"Downloaded {username} - {headline} - {user_photo_url}")

    else:
        print(f"Error fetching page {page_id}: {response.status_code}")
