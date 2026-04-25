
import requests
from bs4 import BeautifulSoup

base_url = "http://example.com?id="
total_pages = 100

# List to store user data
user_data = []

for page_id in range(1, total_pages + 1):
    url = f"{base_url}{page_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        users = soup.find_all('a')
        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Store the user info
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output the gathered data
for user in user_data:
    print(f"User Photo: {user['photo']}, Name: {user['name']}, Title: {user['title']}")
