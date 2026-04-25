
import requests
from bs4 import BeautifulSoup

def crawl_users():
    base_url = 'https://example.com?id='
    users = []

    for page_id in range(1, 101):  # Loop through pages 1 to 100
        response = requests.get(base_url + str(page_id))
        soup = BeautifulSoup(response.content, 'html.parser')

        for user in soup.find_all('a', href=True):  # Locate user links
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                users.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

    return users

# Output example
if __name__ == "__main__":
    user_data = crawl_users()
    for user in user_data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
