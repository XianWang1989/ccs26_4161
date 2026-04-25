
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
base_url = "https://example.com?id="

# List to hold user information
users = []

# Loop through page IDs from 1 to 100
for page_id in range(1, 101):
    # Construct the URL for the current page
    url = f"{base_url}{page_id}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check for a successful response
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        user_entries = soup.find_all('div', class_='user-entry')  # Adjust the class based on the actual structure

        for entry in user_entries:
            # Extract user photo, name, and title
            user_photo = entry.find('img')['src']
            user_name = entry.find('h1', class_='username').text
            user_title = entry.find('p', class_='headline').text

            # Append user data to the list
            users.append({
                'photo': user_photo,
                'name': user_name,
                'title': user_title
            })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output the user data collected
for user in users:
    print(f"{user['name']} - {user['title']}: {user['photo']}")
