
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "http://example.com?id="

# Output directory for images
output_dir = "user_images"
os.makedirs(output_dir, exist_ok=True)

for page_id in range(1, 101):
    # Construct the URL for the current page
    url = f"{base_url}{page_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user containers (adjust the selector based on the actual HTML structure)
        users = soup.select("a[href^='/']")  # Assuming <a> tags contain user links

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next(class_='username').text
            headline = user.find_next(class_='headline').text

            # Download the user photo
            img_url = user_photo  # Adjust if needed, e.g., add base URL
            img_response = requests.get(img_url)
            img_name = os.path.join(output_dir, f"{username}.jpg")

            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Output the user information (you can adapt this to your needs)
            print(f"User: {username}, Title: {headline}, Photo saved as: {img_name}")

    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")
