
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, num_pages):
    users_data = []

    for page_id in range(1, num_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            for user in soup.select('a'):
                img_tag = user.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    users_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline
                    })

    return users_data

def output_to_site(users_data):
    # This function could be modified to output the data to another site
    for user in users_data:
        print(f"<a href='{user['photo']}'><img src='{user['photo']}'></a>")
        print(f"<h1 class='username'>{user['name']}</h1>")
        print(f"<p class='headline'>{user['title']}</p>")

# Change 'example.com' to your target site
base_url = "http://example.com"
num_pages = 100

users_data = crawl_users(base_url, num_pages)
output_to_site(users_data)
