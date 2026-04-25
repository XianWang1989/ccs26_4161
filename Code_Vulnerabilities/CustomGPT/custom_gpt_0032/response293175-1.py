
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site you're crawling
base_url = "https://example.com?id="

# Output folder for images and data
output_folder = "user_data"
os.makedirs(output_folder, exist_ok=True)

for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            user_name = user.find_next('h1', class_='username').text
            user_title = user.find_next('p', class_='headline').text

            # Output user data
            print(f"Name: {user_name}, Title: {user_title}, Photo URL: {user_photo}")

            # Download user photo
            img_response = requests.get(user_photo)
            if img_response.status_code == 200:
                img_name = os.path.join(output_folder, f"{user_name.replace(' ', '_')}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

    else:
        print(f"Failed to retrieve page {page_id}")

print("Crawling completed!")
