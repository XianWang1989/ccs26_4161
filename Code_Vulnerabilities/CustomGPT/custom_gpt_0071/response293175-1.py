
import requests
from bs4 import BeautifulSoup
import os

# Function to fetch user data from a given page
def fetch_user_data(page_id):
    url = f"https://example.com?id={page_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    users = []

    # Find all user elements
    for user_div in soup.find_all('div', class_='user'):  # assuming users are wrapped in a div with class 'user'
        img_tag = user_div.find('img')
        name_tag = user_div.find('h1', class_='username')
        title_tag = user_div.find('p', class_='headline')

        if img_tag and name_tag and title_tag:
            user_data = {
                'photo': img_tag['src'],
                'name': name_tag.text,
                'title': title_tag.text
            }
            users.append(user_data)

    return users

# Main function to crawl the site
def crawl_site():
    all_users = []
    for page_id in range(1, 101):  # Crawling pages from 1 to 100
        print(f'Fetching data from page {page_id}...')
        user_data = fetch_user_data(page_id)
        all_users.extend(user_data)

    # Output the fetched data
    for user in all_users:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")

    return all_users

if __name__ == "__main__":
    crawl_site()
