
import requests
from bs4 import BeautifulSoup
import os

# Base URL for crawling
base_url = "http://example.com?id="
output_dir = "downloaded_images"

# Create directory for images
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to crawl pages and collect user data
def crawl_users(num_pages):
    user_data = []

    for page_id in range(1, num_pages + 1):
        url = f"{base_url}{page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user elements
            users = soup.find_all('a', href=True)

            for user in users:
                img_tag = user.find('img')
                user_photo = img_tag['src'] if img_tag else None
                username_tag = user.find_next('h1', class_='username')
                headline_tag = user.find_next('p', class_='headline')

                username = username_tag.text if username_tag else 'Unknown'
                headline = headline_tag.text if headline_tag else 'No Title'

                # Store user data
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

                # Optionally download the image
                if user_photo:
                    download_image(user_photo, username)

    return user_data

# Function to download images
def download_image(url, username):
    try:
        img_response = requests.get(url)
        if img_response.status_code == 200:
            file_path = os.path.join(output_dir, f"{username.replace(' ', '_')}.jpg")
            with open(file_path, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded: {file_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Main execution
if __name__ == "__main__":
    user_data = crawl_users(100)
    print(user_data)  # Output the collected user data
