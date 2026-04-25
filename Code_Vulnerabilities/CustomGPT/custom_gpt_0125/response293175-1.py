
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "http://example.com?id="

# Loop through the first 100 pages
for page_id in range(1, 101):
    response = requests.get(base_url + str(page_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the user containers (Assuming they are within a div with class 'user')
    users = soup.find_all('div', class_='user')

    for user in users:
        # Extract user details
        photo = user.find('img')['src']
        name = user.find('h1', class_='username').text
        title = user.find('p', class_='headline').text

        # Output the content
        print(f"Name: {name}, Title: {title}, Photo URL: {photo}")
