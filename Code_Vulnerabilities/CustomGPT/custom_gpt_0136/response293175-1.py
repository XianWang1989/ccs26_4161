
import requests
from bs4 import BeautifulSoup

# Function to crawl a page and extract user data
def crawl_users(page_id):
    url = f"http://example.com?id={page_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    users = []

    # Find all user entries; assuming they are contained within 'a' tags
    for user in soup.find_all('a', href=True):
        img_tag = user.find('img')
        username_tag = user.find_next('h1', class_='username')
        headline_tag = user.find_next('p', class_='headline')

        if img_tag and username_tag and headline_tag:
            user_data = {
                'photo': img_tag['src'],
                'name': username_tag.text.strip(),
                'title': headline_tag.text.strip()
            }
            users.append(user_data)

    return users

# Function to crawl multiple pages
def crawl_multiple_pages(start_page, end_page):
    all_users = []
    for page_id in range(start_page, end_page + 1):
        all_users.extend(crawl_users(page_id))
    return all_users

# Example usage: crawl pages 1 to 100
all_user_data = crawl_multiple_pages(1, 100)

# Output the collected user data (could also save to a file or a database)
for user in all_user_data:
    print(user)
