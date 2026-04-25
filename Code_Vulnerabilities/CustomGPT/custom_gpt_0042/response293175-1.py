
import requests
from bs4 import BeautifulSoup

# Base URL for the site
base_url = 'https://example.com?id={}'

# List to store user data
user_data = []

# Loop through pages 1 to 100
for page_id in range(1, 101):
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user elements on the page
        users = soup.find_all('a', href=True)  # Modify this if needed

        for user in users:
            image = user.find('img')
            if image:
                user_photo = image['src']
                username = user.find_next('h1', class_='username').text.strip()
                headline = user.find_next('p', class_='headline').text.strip()

                # Append user information to the list
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

# Output the user data
for user in user_data:
    print(user)
