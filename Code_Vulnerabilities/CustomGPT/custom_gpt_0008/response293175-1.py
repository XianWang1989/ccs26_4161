
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('user_photos', exist_ok=True)

# Base URL
base_url = "http://example.com?id={}"

# Loop through all page IDs
for page_id in range(1, 101):
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (Adjust selector based on actual HTML structure)
        users = soup.find_all('a', href=True)  # Adjust selector as necessary

        for user in users:
            # Extract user photo URL, username, and headline
            img_tag = user.find('img')
            username = user.find_next('h1', class_='username')
            headline = user.find_next('p', class_='headline')

            if img_tag and username and headline:
                user_photo = img_tag['src']
                user_name = username.text.strip()
                user_title = headline.text.strip()

                # Download the image
                img_response = requests.get(user_photo)
                if img_response.status_code == 200:
                    img_name = os.path.join('user_photos', f"{user_name}.jpg")
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)

                # Output the user data (for example, printing it)
                print(f"Name: {user_name}, Title: {user_title}, Photo saved as: {img_name}")

    else:
        print(f"Failed to retrieve page {page_id}: Status code {response.status_code}")
