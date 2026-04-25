
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = 'http://example.com?id='

# Directory to save images
os.makedirs('user_images', exist_ok=True)

for i in range(1, 101):  # Loop from page id 1 to 100
    url = f"{base_url}{i}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        users = soup.find_all('a')  # Find all user links
        for user in users:
            img_tag = user.find('img')  # Get the user photo
            if img_tag and 'src' in img_tag.attrs:
                img_url = img_tag['src']
                img_name = os.path.join('user_images', img_url.split('/')[-1])

                # Download the image
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(img_name, 'wb') as f:
                        f.write(img_response.content)

            # Extract username and title
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Output user data (you can modify this to save it elsewhere)
            print(f'User: {username}, Title: {headline}, Image: {img_name}')

    else:
        print(f"Failed to retrieve page {i}. Status code: {response.status_code}")
