
import requests
from bs4 import BeautifulSoup
import os

# Function to download images
def download_image(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(directory, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)

# Main crawling function
def crawl_users(base_url, num_pages):
    user_data = []
    os.makedirs('images', exist_ok=True)  # Folder to store images

    for page in range(1, num_pages + 1):
        response = requests.get(f"{base_url}?id={page}")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract user elements
        users = soup.find_all('a', href=True)
        for user in users:
            img_tag = user.find('img')
            if img_tag:
                img_url = img_tag['src']
                download_image(img_url, 'images')

                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                user_data.append({
                    'image': img_url,
                    'name': username,
                    'title': headline
                })

    return user_data

# Usage
if __name__ == "__main__":
    base_url = 'http://example.com'
    num_pages = 100
    users = crawl_users(base_url, num_pages)

    # Output data (for example, printing)
    for user in users:
        print(f"Name: {user['name']}, Title: {user['title']}, Image: {user['image']}")
