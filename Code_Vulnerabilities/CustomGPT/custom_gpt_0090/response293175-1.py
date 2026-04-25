
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to store downloaded images
os.makedirs('user_photos', exist_ok=True)

def crawl_users(base_url, pages):
    for page_id in range(1, pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    img_url = img_tag['src']
                    img_name = img_url.split('/')[-1]

                    # Download the image
                    img_response = requests.get(img_url)
                    if img_response.status_code == 200:
                        with open(f'user_photos/{img_name}', 'wb') as img_file:
                            img_file.write(img_response.content)

                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                print(f'Name: {username}, Title: {headline}')

# Example usage
base_url = 'http://example.com'
crawl_users(base_url, 100)
