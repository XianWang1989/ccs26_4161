
import requests
from bs4 import BeautifulSoup

# Base URL of the website
base_url = 'https://example.com?id={}'

# Storage for user information
users = []

# Loop through pages 1 to 100
for page_id in range(1, 101):
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries on the page
        for user in soup.select('a[href^="/"]'):
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            title = user.find_next('p', class_='headline').text

            # Append user data to the list
            users.append({
                'photo': user_photo,
                'name': username,
                'title': title
            })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output user data (example: print or save as needed)
for u in users:
    print(f"Name: {u['name']}, Title: {u['title']}, Photo URL: {u['photo']}")
