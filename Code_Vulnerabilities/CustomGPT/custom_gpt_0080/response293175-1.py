
import requests
from bs4 import BeautifulSoup

# Function to crawl the pages and extract user data
def crawl_users(base_url):
    users_data = []

    for page_id in range(1, 101):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a')  # Assuming each user is within an anchor tag

            for user in users:
                try:
                    # Extract user details
                    user_photo = user.find('img')['src']      # User photo URL
                    username = user.find_next('h1', class_='username').text.strip()  # Username
                    headline = user.find_next('p', class_='headline').text.strip()   # Headline

                    users_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline
                    })
                except Exception as e:
                    print(f"Error extracting data for a user: {e}")

    return users_data

# Base URL of the site to crawl
base_url = 'https://example.com'
user_data = crawl_users(base_url)

# Output the data (you can modify this part to save or display elsewhere)
for user in user_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
