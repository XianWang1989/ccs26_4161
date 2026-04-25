
import requests
from bs4 import BeautifulSoup

def crawl_example_site(base_url, start_id, end_id):
    all_users = []

    for id in range(start_id, end_id + 1):
        response = requests.get(f"{base_url}?id={id}")

        if response.status_code != 200:
            print(f"Failed to fetch page {id}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        users = soup.find_all('a')  # Find all user links

        for user in users:
            user_data = {}
            user_image = user.find('img')
            user_name = soup.find('h1', class_='username')
            user_title = soup.find('p', class_='headline')

            if user_image:
                user_data['photo'] = user_image['src']
            if user_name:
                user_data['name'] = user_name.text
            if user_title:
                user_data['title'] = user_title.text

            all_users.append(user_data)

    return all_users

# Usage
base_url = "https://example.com"
user_data = crawl_example_site(base_url, 1, 100)
print(user_data)
