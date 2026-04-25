
import requests
from bs4 import BeautifulSoup

# Function to fetch user data from a given page
def fetch_users_data(page_id):
    url = f"http://example.com?id={page_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page: {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    users = []

    # Find all user blocks based on the provided HTML structure
    for user_block in soup.find_all('a', href=True):
        user_photo = user_block.find('img')['src']
        username = user_block.find_next_sibling('h1', class_='username').text
        headline = user_block.find_next_sibling('p', class_='headline').text

        # Store user data
        users.append({
            'photo': user_photo,
            'name': username,
            'title': headline
        })

    return users

# Main function to crawl through multiple pages
def main():
    all_users = []

    # Crawl pages from 1 to 100
    for page_id in range(1, 101):
        users_data = fetch_users_data(page_id)
        all_users.extend(users_data)

    # Print or output the collected user data
    for user in all_users:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")

# Run the crawler
if __name__ == '__main__':
    main()
