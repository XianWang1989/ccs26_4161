
import requests
from bs4 import BeautifulSoup

# Base URL for the site
base_url = "http://example.com?id={}"

# Function to crawl user pages
def crawl_users():
    users_data = []

    for page_id in range(1, 101):  # Iterate through pages 1 to 100
        url = base_url.format(page_id)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user blocks (update selectors based on actual HTML structure)
            user_blocks = soup.find_all('div', class_='user-block')  # Example class

            for user in user_blocks:
                # Extract user photo, name, and title
                user_photo = user.find('img')['src']
                username = user.find('h1', class_='username').text.strip()
                title = user.find('p', class_='headline').text.strip()

                # Append user data to the list
                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': title
                })
        else:
            print(f"Failed to retrieve page {page_id}")

    return users_data

# Function to output data on another site (stub for demonstration)
def output_to_site(users):
    # Implement the logic to send 'users' data to another site
    for user in users:
        print(f"User: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")

if __name__ == "__main__":
    users = crawl_users()
    output_to_site(users)
