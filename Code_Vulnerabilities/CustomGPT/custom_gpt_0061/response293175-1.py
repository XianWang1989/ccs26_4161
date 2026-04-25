
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Base URL for the site
base_url = 'https://example.com?id={}'

for page_id in range(1, 101):  # Loop through pages 1 to 100
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user containers (assuming each user is within a specific class)
        user_containers = soup.find_all('a', href=True)

        for user in user_containers:
            # Get user photo URL
            img_tag = user.find('img')
            if img_tag:
                img_url = img_tag['src']
                img_response = requests.get(img_url)

                if img_response.status_code == 200:
                    img_name = os.path.join('user_images', os.path.basename(img_url))
                    with open(img_name, 'wb') as f:
                        f.write(img_response.content)  # Save the image

            # Get username
            username_tag = user.find_next('h1', class_='username')
            username = username_tag.get_text(strip=True) if username_tag else 'N/A'

            # Get title
            headline_tag = user.find_next('p', class_='headline')
            headline = headline_tag.get_text(strip=True) if headline_tag else 'N/A'

            # Output the user data
            print(f'Username: {username}, Title: {headline}, Image saved as: {img_name}')

    else:
        print(f'Failed to retrieve page {page_id}: {response.status_code}')
