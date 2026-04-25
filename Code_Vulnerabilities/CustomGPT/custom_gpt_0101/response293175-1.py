
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

for page_id in range(1, 101):
    url = f'http://example.com?id={page_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    users = soup.find_all('a')
    for user in users:
        img_tag = user.find('img')
        if img_tag:
            img_url = img_tag['src']
            img_name = os.path.join('user_images', os.path.basename(img_url))
            img_data = requests.get(img_url).content

            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)

        username = user.find_next('h1', class_='username')
        headline = user.find_next('p', class_='headline')

        if username and headline:
            print(f'User: {username.text}, Title: {headline.text}')
