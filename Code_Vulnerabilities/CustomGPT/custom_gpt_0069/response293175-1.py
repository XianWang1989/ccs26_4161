
import requests
from bs4 import BeautifulSoup

def crawl_user_data(base_url, max_id):
    user_data = []

    for page_id in range(1, max_id + 1):
        response = requests.get(f"{base_url}?id={page_id}")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries in the page
        users = soup.find_all('a')  # Assuming user links are in <a> tags

        for user in users:
            img_tag = user.find('img')  # Finding the image tag
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

    return user_data

def output_user_data(user_data):
    # Output the data however you wish, here we'll just print it
    for user in user_data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")

if __name__ == "__main__":
    base_url = 'http://example.com'
    max_id = 100
    user_data = crawl_user_data(base_url, max_id)
    output_user_data(user_data)
