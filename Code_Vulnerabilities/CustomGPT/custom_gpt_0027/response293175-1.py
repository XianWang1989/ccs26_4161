
import requests
from bs4 import BeautifulSoup
import os

# Base URL to fetch users
base_url = 'http://example.com?id={}'

# Create a directory to save images
os.makedirs('user_images', exist_ok=True)

# List to hold user data
user_data = []

# Loop through each page (1-100)
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user sections in the page
    users = soup.select('a[href^="/"][img],[h1.username],[p.headline]')

    for user in users:
        # Extract user photo URL
        photo_tag = user.find('img')
        photo_url = photo_tag['src'] if photo_tag else None

        # Extract username and headline
        username = user.find('h1', class_='username').text if user.find('h1', class_='username') else "Unknown"
        headline = user.find('p', class_='headline').text if user.find('p', class_='headline') else "No title"

        if photo_url:
            # Save or download the image
            img_response = requests.get(photo_url)
            img_name = os.path.join('user_images', os.path.basename(photo_url))
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)

        # Store user info
        user_data.append({
            'photo': photo_url,
            'username': username,
            'headline': headline
        })

# Output the user data (or you could insert it into a database or another site)
for user in user_data:
    print(user)
