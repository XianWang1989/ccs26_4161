
import requests
from bs4 import BeautifulSoup
import os

def download_images(user_data):
    for user in user_data:
        img_url = user['photo']
        img_name = os.path.join('images', os.path.basename(img_url))

        # Download the image
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_name, 'wb') as f:
                f.write(response.content)

def crawl_users(base_url, total_pages):
    user_data = []

    for page in range(1, total_pages + 1):
        response = requests.get(f"{base_url}?id={page}")
        soup = BeautifulSoup(response.content, 'html.parser')

        users = soup.find_all('a', href=True)  # Find all user links
        for user in users:
            photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            user_info = {
                'photo': photo,
                'name': username,
                'title': headline
            }
            user_data.append(user_info)

    return user_data

if __name__ == "__main__":
    base_url = "http://example.com"
    total_pages = 100

    # Create a directory for images
    os.makedirs('images', exist_ok=True)

    user_data = crawl_users(base_url, total_pages)
    download_images(user_data)

    # Output to another site or save data as needed
    for user in user_data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
