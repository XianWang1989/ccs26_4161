
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the target site
base_url = 'http://example.com?id='
output_dir = 'output_images'

# Create a directory to save images
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the pages from 1 to 100
for page_id in range(1, 101):
    # Request the page
    response = requests.get(base_url + str(page_id))

    if response.status_code != 200:
        print(f"Failed to retrieve page {page_id}. Status code: {response.status_code}")
        continue

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries (replace with the actual selector if different)
    users = soup.find_all('a', href=True)

    for user in users:
        # Extract user photo
        img_tag = user.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            img_name = os.path.join(output_dir, os.path.basename(img_url))

            # Download the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)
            else:
                print(f"Failed to download image from {img_url}")

        # Extracting user name and title
        username_tag = user.find_next('h1', class_='username')
        headline_tag = user.find_next('p', class_='headline')

        username = username_tag.text.strip() if username_tag else 'No Name'
        headline = headline_tag.text.strip() if headline_tag else 'No Title'

        print(f'Username: {username}, Title: {headline}')

print("Crawling complete.")
