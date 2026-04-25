
import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Loop through the pages
for page_id in range(1, 101):  # Adjust the range for the number of pages
    url = f'https://example.com?id={page_id}'
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user elements
        users = soup.find_all('a', href=True)  # Adjust selector based on actual HTML
        for user in users:
            img_tag = user.find('img')
            name_tag = user.find_next('h1', class_='username')
            title_tag = name_tag.find_next('p', class_='headline')

            if img_tag and name_tag and title_tag:
                image_url = img_tag['src']
                user_name = name_tag.text.strip()
                user_title = title_tag.text.strip()

                # Save image
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    with open(f'user_images/{user_name}.jpg', 'wb') as img_file:
                        img_file.write(image_response.content)

                # Output user data
                print(f'Name: {user_name}, Title: {user_title}, Image saved as: {user_name}.jpg')

    else:
        print(f'Failed to retrieve page: {url}')
