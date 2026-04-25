
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = "http://example.com?id={}"

# Directory to save the downloaded images
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

# Loop through the IDs from 1 to 100
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user cards on the page
        user_cards = soup.find_all('a', href=True)
        for card in user_cards:
            # Get user photo, name and title
            img_tag = card.find('img')
            username_tag = card.find_next('h1', class_='username')
            headline_tag = card.find_next('p', class_='headline')

            if img_tag and username_tag and headline_tag:
                user_photo = img_tag['src']
                username = username_tag.text.strip()
                headline = headline_tag.text.strip()

                # Save the user photo
                img_response = requests.get(user_photo)
                if img_response.status_code == 200:
                    img_filename = os.path.join(output_dir, f"{username}.jpg")
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)

                # Output the user data
                print(f"Name: {username}, Title: {headline}, Photo saved as: {img_filename}")
    else:
        print(f"Failed to fetch page with id {page_id}")
