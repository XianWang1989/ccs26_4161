
import requests
from bs4 import BeautifulSoup
import os
import shutil

# Base URL of the site
base_url = 'https://example.com?id={}'

# Directory to save images
output_dir = 'user_images'
os.makedirs(output_dir, exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                img_url = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Download the image
                img_response = requests.get(img_url, stream=True)
                if img_response.status_code == 200:
                    img_path = os.path.join(output_dir, f"{username}.jpg")
                    with open(img_path, 'wb') as img_file:
                        shutil.copyfileobj(img_response.raw, img_file)
                    print(f"Downloaded: {username}, {headline} - {img_url}")

    else:
        print(f"Failed to retrieve page {page_id}")

print("Crawling complete!")
