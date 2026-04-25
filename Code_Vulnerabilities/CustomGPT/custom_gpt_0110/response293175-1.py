
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Base URL for the pages you want to crawl
base_url = 'https://example.com?id={}'

# Loop through the pages
for page_id in range(1, 101):
    # Make a request to the current page
    response = requests.get(base_url.format(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all users on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Download the user photo
            photo_response = requests.get(user_photo)
            if photo_response.status_code == 200:
                with open(os.path.join('user_images', f"{username}.jpg"), 'wb') as img_file:
                    img_file.write(photo_response.content)
                print(f'Downloaded {username}\'s photo.')
            else:
                print(f'Failed to download {user_photo}.')

            # Output the data
            print(f'Username: {username}, Headline: {headline}')
    else:
        print(f'Failed to retrieve page {page_id}. Status code: {response.status_code}')
