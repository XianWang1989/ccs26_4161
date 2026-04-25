
import requests
from bs4 import BeautifulSoup
import os

# Set up the base URL and the directory to save images
BASE_URL = "https://example.com?id="
OUTPUT_DIR = "downloaded_images"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to crawl and extract user data
def crawl_and_extract_data(total_pages):
    user_data = []

    for page_id in range(1, total_pages + 1):
        response = requests.get(BASE_URL + str(page_id))
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a', href=True)

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Save the image
                img_response = requests.get(user_photo)
                img_name = os.path.join(OUTPUT_DIR, os.path.basename(user_photo))
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

                # Append user data
                user_data.append({
                    'name': username,
                    'title': headline,
                    'photo': img_name
                })

    return user_data

# Execute the crawler
if __name__ == "__main__":
    total_pages = 100
    user_data = crawl_and_extract_data(total_pages)

    # Output user data to another site or file
    for user in user_data:
        print(user)

