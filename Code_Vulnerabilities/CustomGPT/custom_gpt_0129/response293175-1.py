
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
base_url = 'http://example.com?id='

# Loop through the range of IDs you want to crawl
for i in range(1, 101):
    # Construct the URL for each page
    url = f'{base_url}{i}'

    # Send a request to the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user containers (you might need to adjust the selector based on the actual HTML structure)
        users = soup.find_all('div', class_='user-container') # Change 'user-container' to your actual user class

        # Loop through each user and extract details
        for user in users:
            # Extract photo, name, and title
            photo = user.find('img')['src'] if user.find('img') else None
            name = user.find('h1', class_='username').text.strip()
            title = user.find('p', class_='headline').text.strip()

            # Output the user data (you can modify this part to save or send this data elsewhere)
            print(f'Name: {name}, Title: {title}, Photo URL: {photo}')
    else:
        print(f'Failed to retrieve page {i}. Status code: {response.status_code}')
