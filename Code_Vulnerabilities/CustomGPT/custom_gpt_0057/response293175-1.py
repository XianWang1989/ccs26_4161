
import requests
from bs4 import BeautifulSoup
import os

output_dir = 'downloaded_images'
os.makedirs(output_dir, exist_ok=True)

for page_id in range(1, 101):
    url = f'https://example.com?id={page_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    users = soup.find_all('a', href=True)

    for user in users:
        img_tag = user.find('img')
        if img_tag:
            img_url = img_tag['src']
            photo_name = os.path.basename(img_url)
            img_response = requests.get(img_url)

            with open(os.path.join(output_dir, photo_name), 'wb') as f:
                f.write(img_response.content)

        username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else 'N/A'
        title = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else 'N/A'

        print(f'Username: {username}, Title: {title}, Photo saved as: {photo_name if img_tag else "No photo"}')

print('Crawling complete.')
