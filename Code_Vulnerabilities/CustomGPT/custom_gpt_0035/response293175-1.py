
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_photos', exist_ok=True)

for page_id in range(1, 101):  # Loop through pages 1 to 100
    url = f'http://example.com?id={page_id}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a', href=True)  # Find user links
        for user in users:
            img = user.find('img')
            if img:
                img_url = img['src']
                img_name = os.path.join('user_photos', img_url.split('/')[-1])

                # Download and save the image
                with open(img_name, 'wb') as f:
                    img_response = requests.get(img_url)
                    f.write(img_response.content)

            username = soup.find('h1', class_='username').text if soup.find('h1', class_='username') else 'No Name'
            headline = soup.find('p', class_='headline').text if soup.find('p', class_='headline') else 'No Title'

            # Print or store the extracted data
            print(f'User: {username}, Title: {headline}, Photo saved as: {img_name}')
    else:
        print(f'Failed to retrieve page {page_id}')
