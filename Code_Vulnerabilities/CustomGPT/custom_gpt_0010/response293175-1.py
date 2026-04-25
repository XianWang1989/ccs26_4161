
import requests
from bs4 import BeautifulSoup

# Function to crawl the pages and extract user information
def crawl_users(base_url, total_pages):
    users = []

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            user_elements = soup.find_all('a', href=True)

            for user in user_elements:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                users.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve page {page_id}")

    return users

# Base URL of the site
base_url = 'https://example.com'
total_pages = 100  # Crawling pages 1 to 100

# Call the function and store the results
user_data = crawl_users(base_url, total_pages)

# Output the data (you can customize this to output to another site)
for user in user_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
