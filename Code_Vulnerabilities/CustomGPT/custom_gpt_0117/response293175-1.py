
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the pages
for page_id in range(1, 101):
    url = f'http://example.com?id={page_id}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)

        for user in users:
            # Extract the user photo URL, name, and title
            img_tag = user.find('img')
            if img_tag:
                photo_url = img_tag['src']
                user_name = user.find_next('h1', class_='username').text
                user_title = user.find_next('p', class_='headline').text

                # Download the photo
                img_response = requests.get(photo_url)
                if img_response.status_code == 200:
                    # Save the image
                    img_name = os.path.join('user_images', f"{user_name}.jpg")
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)

                # Output data
                print(f"Name: {user_name}, Title: {user_title}, Photo: {img_name}")
    else:
        print(f"Failed to retrieve page {page_id}")
