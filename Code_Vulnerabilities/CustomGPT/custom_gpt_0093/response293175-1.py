
import requests
from bs4 import BeautifulSoup
import os

# Define the base URL and the output directory
base_url = 'http://example.com?id='
output_dir = 'downloaded_images'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the pages
for page_id in range(1, 101):  # From id=1 to id=100
    url = f'{base_url}{page_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user containers (assuming users are in a specific container)
    users = soup.find_all('div', class_='user-container')  # Adjust as needed

    for user in users:
        # Extract user photo, name, and title
        photo_tag = user.find('img')
        if photo_tag and 'src' in photo_tag.attrs:
            photo_url = photo_tag['src']
            photo_name = os.path.join(output_dir, photo_url.split('/')[-1])

            # Download the image
            img_response = requests.get(photo_url)
            if img_response.status_code == 200:
                with open(photo_name, 'wb') as img_file:
                    img_file.write(img_response.content)

        name = user.find('h1', class_='username').text.strip()
        title = user.find('p', class_='headline').text.strip()

        # Output user data (adjust this part to output it to another site)
        print(f'User: {name}, Title: {title}, Photo saved as: {photo_name}')
