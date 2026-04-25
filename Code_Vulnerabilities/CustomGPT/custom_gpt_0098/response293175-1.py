
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_photos', exist_ok=True)

def crawl_and_download_images(base_url, start_id, end_id):
    for page_id in range(start_id, end_id + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_id}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        users = soup.find_all('a')  # Assuming user links are in <a> tags
        for user in users:
            img_tag = user.find('img')
            if img_tag and 'src' in img_tag.attrs:
                img_url = img_tag['src']
                username = user.find_next('h1', class_='username').text.strip()
                title = user.find_next('p', class_='headline').text.strip()

                # Download image
                img_data = requests.get(img_url).content
                img_name = os.path.join('user_photos', f"{username.replace(' ', '_')}.jpg")

                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)

                print(f"Downloaded: {img_name}, Name: {username}, Title: {title}")

# Base URL for the site to crawl
base_url = 'http://example.com'
start_id = 1
end_id = 100

crawl_and_download_images(base_url, start_id, end_id)
