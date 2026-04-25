
import requests
from bs4 import BeautifulSoup

# Base URL of the website to crawl
base_url = 'https://example.com?id={}'

# List to store user data
user_data = []

# Loop through the page IDs from 1 to 100
for page_id in range(1, 101):
    # Construct the URL for the current page
    url = base_url.format(page_id)

    # Send a GET request to fetch the HTML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user containers (adjust the selector as per your HTML structure)
        users = soup.find_all('div', class_='user-container')  # Example class name

        # Loop through each user and extract details
        for user in users:
            # Extract user photo, username, and title
            user_photo = user.find('img')['src']
            username = user.find('h1', class_='username').text.strip()
            headline = user.find('p', class_='headline').text.strip()

            # Store the extracted data
            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })
    else:
        print(f"Failed to retrieve page {page_id} due to status code: {response.status_code}")

# Output user data
for user in user_data:
    print(f"<a href='{user['photo']}'><img src='{user['photo']}'></a>")
    print(f"<h1 class='username'>{user['name']}</h1>")
    print(f"<p class='headline'>{user['title']}</p>")
