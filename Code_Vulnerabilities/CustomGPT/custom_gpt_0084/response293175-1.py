
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, start_id, end_id):
    users_data = []

    for user_id in range(start_id, end_id + 1):
        url = f"{base_url}?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a', href=True)

            for user in users:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text
                title = user.find_next('p', class_='headline').text

                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': title
                })

    return users_data

def output_data(users):
    for user in users:
        print(f"User Photo: {user['photo']}, Name: {user['name']}, Title: {user['title']}")

# Configure the base URL and range
base_url = 'https://example.com'
start_id = 1
end_id = 100

# Crawl the data
users = crawl_users(base_url, start_id, end_id)

# Output the data
output_data(users)
