
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

base_url = 'http://example.com?id='

# Loop through the page IDs
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries (adjust selectors as needed)
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']   # Get image source
            username = user.find_next('h1').text   # Get username
            headline = user.find_next('p').text     # Get headline

            # Download and save image
            photo_response = requests.get(user_photo)
            if photo_response.status_code == 200:
                with open(os.path.join('user_images', f"{username}.jpg"), 'wb') as img_file:
                    img_file.write(photo_response.content)

            # Print user info
            print(f"Name: {username}, Title: {headline}, Photo saved.")

    else:
        print(f"Failed to retrieve page {page_id}")
