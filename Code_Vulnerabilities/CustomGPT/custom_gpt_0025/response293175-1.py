
import requests
from bs4 import BeautifulSoup
import os

# Base URL for the pages
base_url = 'http://example.com?id={}'

# Create a directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Function to crawl and extract user data
def crawl_and_extract():
    user_data = []

    for page_id in range(1, 101):  # Looping from 1 to 100
        response = requests.get(base_url.format(page_id))
        soup = BeautifulSoup(response.text, 'html.parser')

        for user in soup.find_all('a', href=True):
            img_tag = user.find('img')
            name_tag = user.find('h1', class_='username')
            title_tag = user.find('p', class_='headline')

            if img_tag and name_tag and title_tag:
                user_photo = img_tag['src']
                user_name = name_tag.text.strip()
                user_title = title_tag.text.strip()

                # Download the image
                download_image(user_photo)

                # Append user data to the list
                user_data.append({
                    'photo': user_photo,
                    'name': user_name,
                    'title': user_title
                })

    return user_data

# Function to download image
def download_image(photo_url):
    # Handle the image download here
    img_name = os.path.join('user_images', photo_url.split('/')[-1])
    img_response = requests.get(photo_url)

    if img_response.status_code == 200:
        with open(img_name, 'wb') as f:
            f.write(img_response.content)

# Run the crawler and extract data
extracted_data = crawl_and_extract()

# Output results (print or save as needed)
for user in extracted_data:
    print(f"Downloaded {user['name']} - {user['title']} - {user['photo']}")

