
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
base_url = "https://example.com?id={}"

# Function to crawl and extract user data from a page
def crawl_users(page_id):
    response = requests.get(base_url.format(page_id))
    soup = BeautifulSoup(response.content, 'html.parser')

    users = []

    # Find all user containers (modify selectors as needed)
    for user_container in soup.find_all('a', href=True):
        img = user_container.find('img')
        username = user_container.find_next('h1', class_='username')
        headline = user_container.find_next('p', class_='headline')

        if img and username and headline:
            user_data = {
                'photo': img['src'],
                'name': username.text.strip(),
                'title': headline.text.strip()
            }
            users.append(user_data)

    return users

# Collect user data across multiple pages
all_users = []
for page_id in range(1, 101):  # Modify range as needed
    all_users.extend(crawl_users(page_id))

# Output the collected data (for example, print it)
for user in all_users:
    print(user)
