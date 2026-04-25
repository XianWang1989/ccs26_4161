
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
BASE_URL = 'http://example.com?id={}'

# Directory to save images
IMAGE_DIR = 'downloaded_images'
os.makedirs(IMAGE_DIR, exist_ok=True)

def crawl_and_download_images():
    for page_id in range(1, 101):  # Loop through pages 1 to 100
        url = BASE_URL.format(page_id)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all user entries on the page
            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    # Extract user photo URL
                    img_url = img_tag['src']
                    # Assuming the full image URL might need to be constructed
                    if not img_url.startswith('http'):
                        img_url = f"http://example.com{img_url}"

                    # Download the image
                    download_image(img_url)

                # Extract username and headline
                username = user.find_next('h1', class_='username').text.strip()
                headline = user.find_next('p', class_='headline').text.strip()

                # Output to another site or print
                print(f'User: {username}, Headline: {headline}')

def download_image(url):
    # Get the image name from the URL
    image_name = url.split('/')[-1]
    image_path = os.path.join(IMAGE_DIR, image_name)

    # Download the image if it doesn't exist
    if not os.path.exists(image_path):
        img_response = requests.get(url)
        if img_response.status_code == 200:
            with open(image_path, 'wb') as img_file:
                img_file.write(img_response.content)
                print(f'Downloaded: {image_name}')
        else:
            print(f'Failed to download: {url}')

if __name__ == '__main__':
    crawl_and_download_images()
