
import requests
from bs4 import BeautifulSoup

# Function to crawl the user pages
def crawl_user_data(base_url, max_id):
    users_data = []

    for user_id in range(1, max_id + 1):
        # Construct the URL for the current page
        url = f"{base_url}?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200:  # Check if the request was successful
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract user information
            users = soup.find_all('a')  # Adjust selector as necessary

            for user in users:
                img = user.find('img')
                if img:
                    user_photo = img['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text
                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

    return users_data

# Usage
base_url = "http://example.com"
max_id = 100  # Total number of pages
data = crawl_user_data(base_url, max_id)

# Output the data into another site or file
for user in data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
