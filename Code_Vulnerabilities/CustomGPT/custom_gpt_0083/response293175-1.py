
import requests
from bs4 import BeautifulSoup
import os

# Create a directory for saving images
os.makedirs('user_photos', exist_ok=True)

# Function to crawl and extract user data
def crawl_users(base_url, page_count):
    user_data = []

    for page_id in range(1, page_count + 1):
        response = requests.get(f"{base_url}?id={page_id}")
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a')  # Adjust if necessary to target user links

        for user in users:
            img_tag = user.find('img')
            username_tag = user.find('h1', class_='username')
            headline_tag = user.find('p', class_='headline')

            if img_tag and username_tag and headline_tag:
                user_data.append({
                    'photo': img_tag['src'],
                    'name': username_tag.text,
                    'title': headline_tag.text
                })

                # Downloading user photo
                img_url = img_tag['src']
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(f"user_photos/{username_tag.text}.jpg", 'wb') as f:
                        f.write(img_response.content)

    return user_data

# Example usage
base_url = 'http://example.com'
page_count = 100
user_info = crawl_users(base_url, page_count)

# Output user info
for user in user_info:
    print(user)
