
import requests
from bs4 import BeautifulSoup
import os

# Define the base URL and the number of pages to crawl
base_url = "http://example.com?id="
total_pages = 100
output_dir = "downloaded_images"

# Create a directory to save the downloaded images
os.makedirs(output_dir, exist_ok=True)

for page in range(1, total_pages + 1):
    # Make a request to each page
    response = requests.get(base_url + str(page))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (assuming they are wrapped in a <div> or some other tag)
        users = soup.find_all('a')

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                # Extract the image source and other user data
                img_url = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Download the image
                img_response = requests.get(img_url)

                # Only save the image if the request was successful
                if img_response.status_code == 200:
                    img_name = os.path.join(output_dir, img_url.split('/')[-1])
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)

                # Output the user data (you can modify this part to send to another site)
                print(f"User: {username}, Title: {headline}, Image saved as: {img_name}")

    else:
        print(f"Failed to retrieve page {page}: Status code {response.status_code}")
