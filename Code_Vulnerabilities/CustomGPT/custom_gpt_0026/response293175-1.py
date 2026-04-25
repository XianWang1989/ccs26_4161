
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

def crawl_site(base_url, total_pages):
    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a')

            for user in users:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text.strip()
                headline = user.find_next('p', class_='headline').text.strip()

                # Download the user photo
                img_response = requests.get(user_photo)
                img_name = os.path.join('user_images', f"{username}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

                print(f"Downloaded {username}: {headline}, Photo: {user_photo}")
        else:
            print(f"Failed to retrieve page {page_id}")

# Example usage
base_url = "http://example.com"
total_pages = 100
crawl_site(base_url, total_pages)
