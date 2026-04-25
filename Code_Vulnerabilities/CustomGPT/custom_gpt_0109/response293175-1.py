
import requests
from bs4 import BeautifulSoup

# Function to crawl and extract user data
def crawl_users(base_url, pages):
    user_data = []

    for i in range(1, pages + 1):
        url = f"{base_url}?id={i}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            users = soup.find_all('a')  # Adjust based on specific structure

            for user in users:
                user_photo = user.find('img')['src'] if user.find('img') else None
                username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else None
                title = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else None

                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': title
                })

    return user_data

# Set the base url and number of pages to crawl
base_url = 'http://example.com'
pages_to_crawl = 100

# Execute the function
all_users = crawl_users(base_url, pages_to_crawl)

# Output the scraped data
for user in all_users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
