
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save the images
os.makedirs('user_images', exist_ok=True)

# Base URL
base_url = 'http://example.com?id='

# Loop through each page
for page_id in range(1, 101):
    url = f"{base_url}{page_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (assuming there's a common class or tag)
        user_containers = soup.find_all('div', class_='user')  # Adjust this to the correct class or tag

        for user in user_containers:
            # Extract user details
            name = user.find('h1', class_='username').text.strip()
            title = user.find('p', class_='headline').text.strip()
            img_url = user.find('img')['src']

            # Create a full image URL if necessary
            if not img_url.startswith('http'):
                img_url = f"http://example.com{img_url}"

            # Download image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(f'user_images/{name.replace(" ", "_")}.jpg', 'wb') as img_file:
                    img_file.write(img_response.content)

            # Output the user details to another site or file
            print(f"User: {name}, Title: {title}, Image: {img_url}")

    else:
        print(f"Failed to retrieve page {page_id} with status {response.status_code}")
