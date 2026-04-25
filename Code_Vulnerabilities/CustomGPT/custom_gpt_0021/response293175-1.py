
import requests
from bs4 import BeautifulSoup
import os

# Function to download an image
def download_image(url, folder='images'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, url.split('/')[-1]), 'wb') as f:
            f.write(response.content)

# Function to crawl pages and extract user data
def crawl_example_site(base_url, pages):
    for page_id in range(1, pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    # Extract user photo URL
                    img_url = img_tag['src']
                    download_image(img_url)

                # Extract username and headline
                username = user.find_next('h1', class_='username')
                headline = user.find_next('p', class_='headline')

                if username and headline:
                    print(f"User: {username.text.strip()}, Headline: {headline.text.strip()}")

if __name__ == "__main__":
    base_url = 'http://example.com'  # Replace with the actual URL
    crawl_example_site(base_url, 100)  # Crawl first 100 pages
