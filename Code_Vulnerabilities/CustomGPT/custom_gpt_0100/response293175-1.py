
import requests
from bs4 import BeautifulSoup

# Base URL of the website
base_url = "https://example.com?id={}"

# List to store user data
user_data = []

# Loop through the pages
for page_id in range(1, 101):
    # Construct the URL
    url = base_url.format(page_id)

    # Make a request to the page
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all user containers
    users = soup.find_all('a', href=True)

    for user in users:
        # Extract user photo, name, and title
        img_tag = user.find('img')
        if img_tag:
            user_photo = img_tag['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Store the extracted data
            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

# Output the user data to another site
for user in user_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
