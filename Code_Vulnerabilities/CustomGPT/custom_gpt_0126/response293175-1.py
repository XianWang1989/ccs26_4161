
import requests
from bs4 import BeautifulSoup
import os

# Create a directory for downloaded images
os.makedirs('user_images', exist_ok=True)

# Base URL
base_url = 'http://example.com?id={}'

# Loop through the specified range of IDs
for i in range(1, 101):
    # Fetch the page content
    response = requests.get(base_url.format(i))

    if response.status_code == 200:
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)

        for user in users:
            # Extract user photo
            img_tag = user.find('img')
            if img_tag:
                img_url = img_tag['src']
                img_name = os.path.basename(img_url)

                # Download the image
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(os.path.join('user_images', img_name), 'wb') as f:
                        f.write(img_response.content)

            # Extract user name and title
            name = user.find_next('h1', class_='username').text
            title = user.find_next('p', class_='headline').text

            # Output the data
            print(f'Name: {name}, Title: {title}, Image: {img_name}')
    else:
        print(f'Failed to fetch page {i}')
