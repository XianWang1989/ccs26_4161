
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

def crawl_and_extract_data(base_url, num_pages):
    user_data = []

    for page_id in range(1, num_pages + 1):
        response = requests.get(f"{base_url}?id={page_id}")
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a', href=True)  # Find all user links

        for user in users:
            img_tag = user.find('img')  # Get user photo
            if img_tag:
                img_src = img_tag['src']
                img_name = os.path.join('user_images', os.path.basename(img_src))
                download_image(img_src, img_name)

            username = user.find_next('h1', class_='username')
            headline = user.find_next('p', class_='headline')

            user_info = {
                'name': username.get_text() if username else 'N/A',
                'headline': headline.get_text() if headline else 'N/A',
                'photo': img_name
            }
            user_data.append(user_info)

    return user_data

def download_image(img_url, img_name):
    img_response = requests.get(img_url)
    with open(img_name, 'wb') as img_file:
        img_file.write(img_response.content)

# Example Usage
base_url = "http://example.com"
num_pages = 100
user_data = crawl_and_extract_data(base_url, num_pages)

# Print the output data or save it to another site
for user in user_data:
    print(user)
