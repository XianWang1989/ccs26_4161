
import requests
from bs4 import BeautifulSoup

# Change this to the base URL you want to scrape
base_url = "https://example.com?id={}"

# Iterate through the page numbers from 1 to 100
for page_id in range(1, 101):
    # Construct the complete URL
    url = base_url.format(page_id)

    # Send a GET request to the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find user elements
        users = soup.find_all('a', href=True)

        for user in users:
            # Get user photo URL
            img_tag = user.find('img')
            user_photo = img_tag['src'] if img_tag else None

            # Get username
            username = user.find_next('h1', class_='username').text.strip() if user.find_next('h1', class_='username') else None

            # Get user title
            headline = user.find_next('p', class_='headline').text.strip() if user.find_next('p', class_='headline') else None

            # Output user data
            print(f'User Photo: {user_photo}, Username: {username}, Headline: {headline}')
    else:
        print(f"Failed to retrieve page {page_id}, status code: {response.status_code}")
