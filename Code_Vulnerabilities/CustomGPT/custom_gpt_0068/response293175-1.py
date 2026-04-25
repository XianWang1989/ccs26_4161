
import requests
from bs4 import BeautifulSoup

# Base URL and number of pages to crawl
base_url = 'https://example.com?id='
num_pages = 100

# List to hold user data
users_data = []

# Loop through each page
for page_id in range(1, num_pages + 1):
    # Fetch the page
    response = requests.get(base_url + str(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        user_entries = soup.select('a[href*="/"]')  # Select anchor tags with href containing "/"

        # Loop through each user entry
        for entry in user_entries:
            user_photo = entry.find('img')['src']  # Get the image source
            username = entry.find_next('h1', class_='username').text  # Get the username
            headline = entry.find_next('p', class_='headline').text  # Get the headline

            # Store the information
            users_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output the gathered data (example: print it, save to a file, etc.)
for user in users_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
