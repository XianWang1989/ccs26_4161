
import requests
from bs4 import BeautifulSoup

base_url = 'http://example.com?id='
user_data = []

# Loop through the range of IDs from 1 to 100
for i in range(1, 101):
    response = requests.get(base_url + str(i))

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries on the page
        users = soup.find_all('a', href=True)

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Append the user information to the list
            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

# Output the collected user data
for data in user_data:
    print(f"Name: {data['name']}, Title: {data['title']}, Photo: {data['photo']}")
