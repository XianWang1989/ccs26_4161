
import requests
from bs4 import BeautifulSoup

# Function to extract user information from a single page
def extract_users(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    users = []

    # Find user details
    for user in soup.find_all('a', href=True):
        img_tag = user.find('img')
        if img_tag:
            user_info = {
                'photo': img_tag['src'],
                'name': user.find_next('h1', class_='username').text,
                'title': user.find_next('p', class_='headline').text
            }
            users.append(user_info)

    return users

# Main function to crawl through pages
def crawl_site(base_url, total_pages):
    all_users = []
    for page_id in range(1, total_pages + 1):
        page_url = f"{base_url}?id={page_id}"
        users = extract_users(page_url)
        all_users.extend(users)

    return all_users

# Usage example
if __name__ == "__main__":
    base_url = "http://example.com"
    total_pages = 100
    user_data = crawl_site(base_url, total_pages)

    # Output the collected data
    for user in user_data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
