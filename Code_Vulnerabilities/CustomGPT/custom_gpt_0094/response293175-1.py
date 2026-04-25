
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Base URL
base_url = "http://example.com?id="

# Loop through pages 1 to 100
for page in range(1, 101):
    response = requests.get(base_url + str(page))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                # Get user name and title
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Output the user data
                print(f"Name: {username}, Title: {headline}, Photo URL: {user_photo}")

                # Download the image
                img_response = requests.get(user_photo)
                if img_response.status_code == 200:
                    img_name = os.path.join('user_images', f"{username}.jpg")
                    with open(img_name, 'wb') as f:
                        f.write(img_response.content)

    else:
        print(f"Failed to retrieve page {page}")

print("Crawling complete.")
