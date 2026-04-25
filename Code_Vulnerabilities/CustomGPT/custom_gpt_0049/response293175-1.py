
import requests
from bs4 import BeautifulSoup

# Function to crawl user pages
def crawl_users(start_id, end_id):
    users_data = []

    for user_id in range(start_id, end_id + 1):
        url = f'http://example.com?id={user_id}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all user entries in the HTML
            user_entries = soup.find_all('a')  # Adjust the selector as needed

            for entry in user_entries:
                user_photo = entry.find('img')['src'] if entry.find('img') else 'No photo'
                username = entry.find_next('h1', class_='username').text if entry.find_next('h1', class_='username') else 'No name'
                headline = entry.find_next('p', class_='headline').text if entry.find_next('p', class_='headline') else 'No title'

                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve data from page id: {user_id}")

    return users_data

# Crawling users from id 1 to 100
users = crawl_users(1, 100)

# Outputting the data; here you can choose how to display or store this
for user in users:
    print(f"Photo: {user['photo']}, Name: {user['name']}, Title: {user['title']}")
