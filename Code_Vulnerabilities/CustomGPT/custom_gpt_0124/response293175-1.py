
import requests
from bs4 import BeautifulSoup
import os

# Base URL for the site
base_url = 'http://example.com?id='

# Create a directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Loop through the first 100 pages
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all users on the page
    users = soup.find_all('a', href=True)
    for user in users:
        img_tag = user.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Output the user information
            print(f'User: {username}, Title: {headline}, Image URL: {img_url}')

            # Download the image
            img_response = requests.get(img_url)
            img_name = os.path.join('user_images', f'{username}.jpg')
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

print('Crawling completed!')
