
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = "https://example.com?id={}"

# Function to download an image
def download_image(url, folder, filename):
    img_response = requests.get(url)
    if img_response.status_code == 200:
        with open(os.path.join(folder, filename), 'wb') as image_file:
            image_file.write(img_response.content)

# Create a directory to store downloaded images
os.makedirs('user_images', exist_ok=True)

# Loop through the first 100 pages
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract user data
        user_links = soup.find_all('a')  # All user links
        usernames = soup.find_all('h1', class_='username')
        headlines = soup.find_all('p', class_='headline')

        for link, username, headline in zip(user_links, usernames, headlines):
            user_photo_url = link.find('img')['src']
            user_name = username.text.strip()
            user_title = headline.text.strip()

            # Print user data
            print(f"Name: {user_name}, Title: {user_title}")

            # Optional: Download the user photo
            if user_photo_url:
                filename = os.path.basename(user_photo_url)
                download_image(user_photo_url, 'user_images', filename)
    else:
        print(f"Failed to access page {page_id}")

print("Crawling completed!")
