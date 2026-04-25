
import requests
from bs4 import BeautifulSoup

# Function to crawl and extract user data
def crawl_users(base_url, total_pages):
    user_data = []  # List to store user details

    for page_id in range(1, total_pages + 1):
        # Construct the URL
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all user elements based on the provided structure
            users = soup.find_all('a', href=True)

            for user in users:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text.strip()
                headline = user.find_next('p', class_='headline').text.strip()

                # Append the data to the user_data list
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve page {page_id}")

    return user_data

# Base URL for the crawling site
base_url = 'https://example.com'
total_pages = 100

# Call the function and store the results
user_list = crawl_users(base_url, total_pages)

# Output user data
for user in user_list:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
