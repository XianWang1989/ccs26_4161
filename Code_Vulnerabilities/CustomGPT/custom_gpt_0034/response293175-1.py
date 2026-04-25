
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
base_url = "http://example.com?id="

# Function to crawl and extract user data
def crawl_users(start_id, end_id):
    users_data = []

    for user_id in range(start_id, end_id + 1):
        response = requests.get(base_url + str(user_id))
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (assuming they are in a specific class)
        user_containers = soup.find_all('div', class_='user-container')

        for user in user_containers:
            photo = user.find('img')['src']
            name = user.find('h1', class_='username').text
            title = user.find('p', class_='headline').text
            users_data.append({'photo': photo, 'name': name, 'title': title})

    return users_data

# Example usage
all_users = crawl_users(1, 100)

# Output users data (you can modify this to save or display it on another site)
for user in all_users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
