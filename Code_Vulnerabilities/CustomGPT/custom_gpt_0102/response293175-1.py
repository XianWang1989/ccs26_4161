
import requests
from bs4 import BeautifulSoup
import os

# URL template for the pages
url_template = "http://example.com?id={}"

# Directory to save images
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

# Loop through pages from 1 to 100
for page_id in range(1, 101):
    url = url_template.format(page_id)

    # Send a request to the page
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user blocks on the page
        users = soup.find_all('div', class_='user_block')  # Adjust according to the site

        for user in users:
            # Extract user photo, name, and title
            img_tag = user.find('img')
            username = user.find('h1', class_='username').text.strip()
            title = user.find('p', class_='headline').text.strip()

            # Download user photo
            img_url = img_tag['src']
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                img_name = os.path.join(output_dir, f"{username}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

            # Output user details
            print(f"User: {username}, Title: {title}, Photo saved as: {img_name}")

    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")
