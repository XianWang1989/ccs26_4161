
import requests
from bs4 import BeautifulSoup
import os

# URL format for crawling
base_url = 'http://example.com?id={}'

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

for page_id in range(1, 101):  # Loop through pages from 1 to 100
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user containers (assuming there’s a specific class for them)
        users = soup.find_all('div', class_='user-container')  # Adjust as necessary

        for user in users:
            # Extract user photo, name, and title
            user_photo = user.find('img')['src']
            username = user.find('h1', class_='username').text
            headline = user.find('p', class_='headline').text

            # Download the user photo
            img_response = requests.get(user_photo)
            if img_response.status_code == 200:
                img_name = os.path.join('user_images', f"{username}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f'Downloaded {img_name} - {username}: {headline}')
            else:
                print(f'Failed to download image for {username}')
    else:
        print(f'Failed to retrieve page {page_id}: {response.status_code}')
