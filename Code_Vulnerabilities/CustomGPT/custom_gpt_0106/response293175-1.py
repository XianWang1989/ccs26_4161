
import requests
from bs4 import BeautifulSoup

# Base URL for the pages
base_url = "http://example.com?id={}"

# List to store user data
users_data = []

# Crawl through 100 pages
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    # Check if request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)  # Adjust selectors as necessary

        for user in users:
            user_photo = user.find('img')['src']  # Get image source
            username = user.find_next('h1', class_='username').text  # Get username
            headline = user.find_next('p', class_='headline').text  # Get title

            # Store user data
            users_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline,
            })
    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")

# Output collected user data
for user in users_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
