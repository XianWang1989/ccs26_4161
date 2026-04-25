
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "http://example.com?id={} "
# Number of pages to crawl
num_pages = 100

# Function to download an image
def download_image(url, folder_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_path, os.path.basename(url)), 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download image: {url}")
    except Exception as e:
        print(f"Error: {e}")

# Output folder for images
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Crawling through the pages
for page_id in range(1, num_pages + 1):
    # Make a GET request to fetch the raw HTML content
    response = requests.get(base_url.format(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Finding user information
        users = soup.find_all('a', href=True)
        for user in users:
            user_image = user.find('img')
            username = user.find_next('h1', class_='username')
            headline = user.find_next('p', class_='headline')

            if user_image and username and headline:
                # Extract image URL, name, and title
                image_url = user_image['src']
                name = username.text
                title = headline.text

                # Print the user information (to be output somewhere else)
                print(f"Name: {name}, Title: {title}, Image URL: {image_url}")

                # Download the user image
                download_image(image_url, output_folder)
    else:
        print(f"Failed to retrieve page: {response.status_code} for page id {page_id}")
