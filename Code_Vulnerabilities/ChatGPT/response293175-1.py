
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site you want to scrape
BASE_URL = 'http://example.com'
OUTPUT_DIR = 'downloaded_images'

# Create a directory to save images
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to download an image
def download_image(url, img_name):
    try:
        img_data = requests.get(url).content
        with open(os.path.join(OUTPUT_DIR, img_name), 'wb') as img_file:
            img_file.write(img_data)
        print(f'Downloaded: {img_name}')
    except Exception as e:
        print(f'Could not download {img_name}: {e}')

# Loop through the pages from 1 to 100
for page_id in range(1, 101):
    response = requests.get(f'{BASE_URL}?id={page_id}')

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries (modify the selectors based on the actual HTML structure)
        user_entries = soup.find_all('a', href=True)

        for user in user_entries:
            user_photo = user.find('img')['src'] if user.find('img') else None
            username = user.find_next('h1', class_='username').text.strip() if user.find_next('h1', class_='username') else 'Unknown'
            headline = user.find_next('p', class_='headline').text.strip() if user.find_next('p', class_='headline') else 'No Title'

            if user_photo:
                # Constructing the full image URL if the source is relative
                photo_url = user_photo if user_photo.startswith('http') else BASE_URL + user_photo
                img_name = username.replace(" ", "_") + '.jpg'  # Create a valid filename
                download_image(photo_url, img_name)

            # Output the user information (you can modify this part to export in any format)
            print(f'Name: {username}, Title: {headline}')
    else:
        print(f'Failed to retrieve page {page_id}: {response.status_code}')
