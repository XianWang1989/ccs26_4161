
import requests
from bs4 import BeautifulSoup

# Function to scrape user data
def scrape_users():
    all_users = []

    # Iterate through pages 1 to 100
    for page_id in range(1, 101):
        response = requests.get(f'https://example.com?id={page_id}')
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)
        for user in users:
            user_photo = user.img['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text
            all_users.append({'photo': user_photo, 'name': username, 'title': headline})

    return all_users

# Run the scraper
user_data = scrape_users()

# Example output to another site or storage
for user in user_data:
    print(f"User Photo: {user['photo']}, Name: {user['name']}, Title: {user['title']}")
