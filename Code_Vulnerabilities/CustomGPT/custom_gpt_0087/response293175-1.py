
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, start_id, end_id):
    users_data = []

    for user_id in range(start_id, end_id + 1):
        url = f"{base_url}?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a')  # Adjust based on the HTML structure

            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    img_src = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    users_data.append({
                        'photo': img_src,
                        'name': username,
                        'title': headline
                    })

    return users_data

# Usage
base_url = "https://example.com"
users = crawl_users(base_url, 1, 100)

# Output to another site/process as needed
for user in users:
    print(user)
