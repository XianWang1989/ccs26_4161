
import requests
from bs4 import BeautifulSoup

def scrape_users():
    base_url = "http://example.com?id={}"
    user_data = []

    for page_id in range(1, 101):  # From page 1 to 100
        url = base_url.format(page_id)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a')  # Adjust the selectors as needed

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

    return user_data

# Usage
if __name__ == "__main__":
    users = scrape_users()
    for user in users:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
