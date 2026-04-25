
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = "https://example.com?id={}"

# Create a directory to save images
os.makedirs("user_photos", exist_ok=True)

# Function to crawl pages
def crawl_pages():
    for page_id in range(1, 101):
        url = base_url.format(page_id)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            users = soup.find_all('a')  # Adjust based on your HTML structure

            for user in users:
                img_tag = user.find('img')
                username_tag = user.find_next('h1', class_='username')
                headline_tag = username_tag.find_next('p', class_='headline')

                if img_tag and username_tag and headline_tag:
                    user_photo_url = img_tag['src']
                    username = username_tag.text.strip()
                    headline = headline_tag.text.strip()

                    # Download user photo
                    image_response = requests.get(user_photo_url)
                    if image_response.status_code == 200:
                        # Save the image
                        image_path = os.path.join("user_photos", f"{username}.jpg")
                        with open(image_path, 'wb') as img_file:
                            img_file.write(image_response.content)

                    # Output user data
                    print(f'Username: {username}, Title: {headline}, Photo saved: {image_path}')
        else:
            print(f"Failed to retrieve page {page_id}")

if __name__ == "__main__":
    crawl_pages()
