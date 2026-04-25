
import requests
from bs4 import BeautifulSoup

def crawl_user_data(base_url, total_pages):
    user_data = []

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            users = soup.find_all('a', href=True)

            for user in users:
                img_tag = user.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    user_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline
                    })
        else:
            print(f"Failed to retrieve page {page_id}")

    return user_data

if __name__ == "__main__":
    base_url = "https://example.com"
    total_pages = 100
    user_info = crawl_user_data(base_url, total_pages)

    for user in user_info:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
