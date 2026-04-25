
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_photos', exist_ok=True)

# Function to crawl and scrape user data
def crawl_users(base_url):
    for page_id in range(1, 101):  # Pages from id=1 to id=100
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find user entries; update selector as needed
            users = soup.find_all('a', href=True)

            for user in users:
                img_tag = user.find('img')
                if img_tag and 'src' in img_tag.attrs:
                    user_photo = img_tag['src']
                    user_name = user.find_next('h1', class_='username').text
                    user_title = user.find_next('p', class_='headline').text

                    # Download the photo
                    download_image(user_photo, user_name)

                    # Output the user data
                    print(f"Name: {user_name}, Title: {user_title}, Photo: {user_photo}")
        else:
            print(f"Failed to retrieve page {page_id}")

# Function to download images
def download_image(photo_url, user_name):
    response = requests.get(photo_url)
    if response.status_code == 200:
        # Clean the user name for a filename
        filename = f"user_photos/{user_name}.jpg"
        with open(filename, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {photo_url}")

# Start crawling
base_url = 'https://example.com'
crawl_users(base_url)
