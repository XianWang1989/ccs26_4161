
import requests
from bs4 import BeautifulSoup
import os

def fetch_user_data(page_id):
    url = f"http://example.com?id={page_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page_id}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    users = []

    # Modify the selectors based on the actual HTML structure
    for user in soup.select('a[href^="/"]'):
        photo = user.find('img')['src']
        name = user.find_next(class_='username').text
        title = user.find_next('p', class_='headline').text

        users.append({
            'photo': photo,
            'name': name,
            'title': title
        })

    return users

def save_data_to_output(users, output_file='output.txt'):
    with open(output_file, 'a') as f:
        for user in users:
            f.write(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}\n")

if __name__ == "__main__":
    all_users = []

    for i in range(1, 101):
        user_data = fetch_user_data(i)
        all_users.extend(user_data)

    # Optionally, save user data to a file
    save_data_to_output(all_users)

    print(f"Total users fetched: {len(all_users)}")
