
import requests
from bs4 import BeautifulSoup
import os

# Function to crawl the website
def crawl_users(base_url, total_pages, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find user entries
            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                if img_tag and 'src' in img_tag.attrs:
                    img_url = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    title = user.find_next('p', class_='headline').text

                    # Download image
                    download_image(img_url, username, output_directory)

                    # Output user data
                    print(f"User: {username}, Title: {title}")

def download_image(img_url, username, output_directory):
    img_data = requests.get(img_url).content
    filename = f"{username.replace(' ', '_')}.jpg"
    filepath = os.path.join(output_directory, filename)

    with open(filepath, 'wb') as img_file:
        img_file.write(img_data)

# Example usage
base_url = "http://example.com"
total_pages = 100
output_directory = "downloaded_images"

crawl_users(base_url, total_pages, output_directory)
