
import requests
from bs4 import BeautifulSoup
import os

# Base URL and output directory
base_url = "https://example.com?id="
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all users on the page
    users = soup.find_all('a', href=True)  # Assuming <a> contains user info

    for user in users:
        img_tag = user.find('img')
        if img_tag:
            img_url = img_tag['src']
            name = user.find_next('h1', class_='username').text.strip()
            title = user.find_next('p', class_='headline').text.strip()

            # Download the image
            img_response = requests.get(img_url)
            img_name = os.path.join(output_dir, os.path.basename(img_url))

            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output the user data
            print(f"Name: {name}, Title: {title}, Image: {img_name}")

print("Crawling complete.")
