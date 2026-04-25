
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# Function to crawl user pages
def crawl_users(base_url, total_pages):
    user_data = []

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page_id}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Download the user photo
            img_response = requests.get(user_photo)
            img_name = os.path.join('user_images', os.path.basename(user_photo))

            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

            # Append user data
            user_data.append({
                'name': username,
                'title': headline,
                'photo': img_name
            })

    return user_data

# Base URL and total number of pages
base_url = 'http://example.com'  # Replace with the actual site
total_pages = 100

# Run the crawler
users_info = crawl_users(base_url, total_pages)

# Output results
for user in users_info:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo saved at: {user['photo']}")
