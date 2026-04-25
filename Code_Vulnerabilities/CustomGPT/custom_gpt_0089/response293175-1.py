
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = 'http://example.com?id={}'

# Directory to save images
image_dir = 'user_images'
os.makedirs(image_dir, exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user entries on the page
    users = soup.findAll('a', href=True)  # Adjust as necessary

    for user in users:
        user_photo = user.find('img')['src']
        username = user.find_next('h1', class_='username').text
        headline = user.find_next('p', class_='headline').text

        # Full image URL construction (assuming relative URLs)
        image_url = f'http://example.com{user_photo}'

        # Download the image
        img_response = requests.get(image_url)
        img_name = os.path.join(image_dir, f"{username}.jpg")

        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)

        # Output the user data
        print(f'Username: {username}, Headline: {headline}, Image saved as: {img_name}')

# Next steps would involve uploading this data to another site
