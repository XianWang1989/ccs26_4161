
import requests
from bs4 import BeautifulSoup

# Base URL of the site
base_url = 'http://example.com?id={}'

# List to store user data
users_data = []

# Loop through pages 1 to 100
for page_id in range(1, 101):
    # Request the page
    response = requests.get(base_url.format(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user elements
        users = soup.find_all('a')

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Append user data to the list
                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output or save the users' data
for user in users_data:
    print(user)  # You can modify this to save to another site
