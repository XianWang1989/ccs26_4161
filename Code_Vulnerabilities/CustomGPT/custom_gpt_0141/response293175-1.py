
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images if it does not exist
os.makedirs('user_images', exist_ok=True)

# Base URL for crawling the pages
base_url = 'http://example.com?id='

# Loop through the page IDs
for page_id in range(1, 101):  # From 1 to 100
    # Construct the URL for each page
    url = f"{base_url}{page_id}"
    print(f"Crawling page: {url}")

    # Make a GET request to fetch the raw HTML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (assuming they are inside a specific tag/class)
        users = soup.find_all('div', class_='user-container')  # Adjust this according to the site's structure

        # Loop through each user and extract data
        for user in users:
            name = user.find('h1', class_='username').text.strip()
            title = user.find('p', class_='headline').text.strip()
            img_src = user.find('img')['src']

            # Download the image
            img_response = requests.get(img_src)
            if img_response.status_code == 200:
                img_name = os.path.join('user_images', f"{name.replace(' ', '_')}.jpg")
                with open(img_name, 'wb') as image_file:
                    image_file.write(img_response.content)

            # Output the user data
            print(f"Name: {name}, Title: {title}, Image saved as: {img_name}")

    else:
        print(f"Failed to retrieve page {page_id}, status code: {response.status_code}")
