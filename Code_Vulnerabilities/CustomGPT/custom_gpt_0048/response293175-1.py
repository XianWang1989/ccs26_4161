
import requests
from bs4 import BeautifulSoup

# Base URL of the site
base_url = 'http://example.com?id={}'

# List to store user data
users_data = []

# Loop through ID range
for page_id in range(1, 101):
    # Construct the URL for the current page
    url = base_url.format(page_id)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries (adjust selectors as needed)
        user_entries = soup.find_all('a', class_='user-link')  # Adjust class name
        for entry in user_entries:
            user_photo = entry.find('img')['src']
            username = entry.find_next('h1', class_='username').text
            headline = entry.find_next('p', class_='headline').text

            # Append data to users_data list
            users_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })
    else:
        print(f"Failed to retrieve page: {url}")

# Output the collected data
for user in users_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
