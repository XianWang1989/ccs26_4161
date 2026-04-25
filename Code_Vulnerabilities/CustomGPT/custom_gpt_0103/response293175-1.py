
import requests
from bs4 import BeautifulSoup
import os

# Base URL
base_url = "https://example.com?id={}"

# Directory to save images
os.makedirs('user_images', exist_ok=True)

# Loop through the first 100 pages
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find user elements (adjust the selectors as needed)
    user_links = soup.find_all('a', href=True)
    usernames = soup.find_all('h1', class_='username')
    headlines = soup.find_all('p', class_='headline')

    # Extract data
    for link, username, headline in zip(user_links, usernames, headlines):
        user_photo_url = link.img['src']
        user_name = username.text.strip()
        user_title = headline.text.strip()

        # Download user photo
        img_response = requests.get(user_photo_url)
        img_name = os.path.join('user_images', f"{user_name}.jpg")

        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)

        # Output the user data
        print(f"Name: {user_name}, Title: {user_title}, Photo saved as: {img_name}")
