
import requests
from bs4 import BeautifulSoup
import os

# Directory to save images
image_directory = 'user_images'
os.makedirs(image_directory, exist_ok=True)

# Base URL for crawling
base_url = "http://example.com?id={}"

# Loop through each page
for page_id in range(1, 101):  # Pages from 1 to 100
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user data
        user_containers = soup.find_all('div', class_='user-container')  # Adjust based on actual HTML structure

        for user in user_containers:
            img_tag = user.find('img')
            username_tag = user.find('h1', class_='username')
            headline_tag = user.find('p', class_='headline')

            if img_tag and username_tag and headline_tag:
                user_photo = img_tag['src']
                username = username_tag.text.strip()
                headline = headline_tag.text.strip()

                # Download the image
                img_response = requests.get(user_photo)
                img_name = os.path.join(image_directory, f"{username}.jpg")
                with open(img_name, 'wb') as f:
                    f.write(img_response.content)

                # Print or output the user data
                print(f"User: {username}, Title: {headline}, Image: {img_name}")
    else:
        print(f"Failed to retrieve page {page_id} with status code {response.status_code}")
