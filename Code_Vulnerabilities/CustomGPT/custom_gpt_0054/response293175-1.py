
import requests
from bs4 import BeautifulSoup

# Base URL for the site
base_url = "https://example.com?id={}"

# Function to crawl and extract user data
def crawl_users():
    for page_id in range(1, 101):  # Loop through page IDs 1 to 100
        url = base_url.format(page_id)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            users = soup.find_all('a')  # Assuming user links are in <a> tags

            for user in users:
                img = user.find('img')  # Find the <img> tag within <a>
                if img:
                    user_photo = img['src']
                    username = user.find_next('h1', class_='username').text
                    headline = user.find_next('p', class_='headline').text

                    # Output the user data (could be modified to store in a list or DB)
                    print(f"User Photo: {user_photo}, Username: {username}, Title: {headline}")
        else:
            print(f"Failed to retrieve page {page_id}: Status code {response.status_code}")

# Start crawling
crawl_users()
