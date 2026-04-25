
import requests
from bs4 import BeautifulSoup

# Base URL for crawling
base_url = "https://example.com?id={}"

# List to store user data
user_data = []

# Loop through the IDs from 1 to 100
for i in range(1, 101):
    # Fetch the page content
    response = requests.get(base_url.format(i))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user elements on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            title = user.find_next('p', class_='headline').text

            # Store the user data
            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': title
            })
    else:
        print(f"Failed to retrieve page {i}")

# Output the user data (could also be saved or posted to another site)
for user in user_data:
    print(user)
