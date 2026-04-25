
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to store images
os.makedirs('user_images', exist_ok=True)

# Base URL
base_url = 'https://example.com?id={}'

# Loop through pages
for page_id in range(1, 101):
    # Construct the URL
    url = base_url.format(page_id)

    # Make a GET request to the page
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)

        for user in users:
            # Extract image source
            img_tag = user.find('img')
            if img_tag and 'src' in img_tag.attrs:
                img_url = img_tag['src']
                img_name = os.path.join('user_images', img_url.split('/')[-1])

                # Download the image
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f'Downloaded: {img_name}')

            # Extract username
            username = user.find_next('h1', class_='username')
            headline = user.find_next('p', class_='headline')

            if username and headline:
                print(f'User: {username.text}, Title: {headline.text}')

    else:
        print(f'Failed to retrieve page {page_id}: Status code {response.status_code}')
