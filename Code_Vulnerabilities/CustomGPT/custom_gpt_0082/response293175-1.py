
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://example.com?id="

# Loop through pages
for page_id in range(1, 101):
    # Construct the full URL
    url = f"{base_url}{page_id}"

    # Send a GET request to fetch the HTML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user elements
        users = soup.find_all('a')

        # Loop through each user element
        for user in users:
            # Extract user photo URL
            img = user.find('img')
            user_photo = img['src'] if img else None

            # Extract username
            username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else "N/A"

            # Extract title
            title = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else "N/A"

            # Output the extracted data
            print(f"User Photo: {user_photo}, Username: {username}, Title: {title}")
    else:
        print(f"Failed to retrieve page {page_id}: Status code {response.status_code}")
