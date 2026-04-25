
import requests
from bs4 import BeautifulSoup
import os

# Base URL and number of pages you want to scrape
base_url = "http://example.com?id={}"
num_pages = 100

# Create directory to save user images
if not os.path.exists("user_images"):
    os.makedirs("user_images")

# Loop through the pages
for page in range(1, num_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries on the page
        user_entries = soup.find_all('a', href=True)

        for entry in user_entries:
            user_photo_tag = entry.find('img')
            username_tag = entry.find('h1', class_='username')
            headline_tag = entry.find('p', class_='headline')

            if user_photo_tag and username_tag and headline_tag:
                # Extract image URL, user name, and title
                user_photo_url = user_photo_tag['src']
                username = username_tag.text
                headline = headline_tag.text

                # Download the image
                image_response = requests.get(user_photo_url)
                if image_response.status_code == 200:
                    image_name = os.path.join("user_images", f"{username}.jpg")
                    with open(image_name, 'wb') as f:
                        f.write(image_response.content)

                # Output the extracted information
                print(f"Name: {username}, Title: {headline}, Image saved as: {image_name}")

    else:
        print(f"Failed to retrieve page {page}: Status code {response.status_code}")
