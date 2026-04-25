
import requests
from bs4 import BeautifulSoup

# Base URL for the pages to crawl
base_url = "http://example.com?id={}"

# Function to crawl user data from a single page
def crawl_page(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    users_data = []

    # Find all user entries on the page
    user_entries = soup.find_all('a', href=True)
    for entry in user_entries:
        user_photo = entry.find('img')
        username = entry.find_next('h1', class_='username')
        headline = username.find_next('p', class_='headline') if username else None

        if user_photo and username and headline:
            users_data.append({
                'photo': user_photo['src'],
                'name': username.text.strip(),
                'title': headline.text.strip()
            })

    return users_data

# Main crawling process
all_users = []
for i in range(1, 101):  # Loop through pages 1 to 100
    page_users = crawl_page(i)
    all_users.extend(page_users)

# Output: Display the crawled data (you can change this to save to another site)
for user in all_users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
