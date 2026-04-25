
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, start_id, end_id):
    user_data = []

    for user_id in range(start_id, end_id + 1):
        url = f"{base_url}?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            users = soup.find_all('a')  # Adjust the selector as needed
            for user in users:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve data from {url}")

    return user_data

# Usage
base_url = 'http://example.com'
data = crawl_users(base_url, 1, 100)

# Output the data (you can modify this part to save or send it to another site)
for user in data:
    print(user)
