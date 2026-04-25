
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = 'https://example.com?id={}'

# Loop through the pages
for page_id in range(1, 101):
    # Fetch the page
    response = requests.get(base_url.format(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user elements (this will depend on the actual HTML structure)
        users = soup.find_all('a', href=True)  # Assuming user links are within <a> tags

        for user in users:
            user_photo = user.find('img')['src']  # Get image source
            username = user.find_next('h1', class_='username').text  # Next h1 for username
            headline = user.find_next('p', class_='headline').text  # Next p for title

            # Output the data (this could be modified to post elsewhere)
            print(f'User: {username}, Title: {headline}, Photo URL: {user_photo}')

# Note: Ensure you have the correct HTML structure and adjust the selectors accordingly.
