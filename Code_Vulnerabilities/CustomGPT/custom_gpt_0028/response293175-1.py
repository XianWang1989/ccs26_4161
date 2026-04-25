
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, num_pages):
    users_data = []

    for page_id in range(1, num_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            user_elements = soup.find_all('a')

            for user_elem in user_elements:
                img_tag = user_elem.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user_elem.find_next('h1', class_='username').text
                    headline = user_elem.find_next('p', class_='headline').text

                    users_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline
                    })

        else:
            print(f"Failed to retrieve page {page_id}: {response.status_code}")

    return users_data

# Example usage
base_url = 'https://example.com'
num_pages = 100
users = crawl_users(base_url, num_pages)

# Output data
for user in users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
