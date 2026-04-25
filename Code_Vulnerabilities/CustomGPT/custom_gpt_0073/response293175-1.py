
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

for page_id in range(1, 101):
    url = f'http://example.com?id={page_id}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a', href=True)  # or a more specific selector
        for user in users:
            img_tag = user.find('img')
            if img_tag:
                img_url = img_tag['src']
                img_name = os.path.basename(img_url)
                img_response = requests.get(img_url)

                # Save the image
                if img_response.status_code == 200:
                    with open(os.path.join('user_images', img_name), 'wb') as img_file:
                        img_file.write(img_response.content)

            username = user.find_next('h1', class_='username')
            headline = user.find_next('p', class_='headline')

            if username and headline:
                print(f"Name: {username.text.strip()}, Title: {headline.text.strip()}")
    else:
        print(f"Failed to retrieve page {page_id}")
