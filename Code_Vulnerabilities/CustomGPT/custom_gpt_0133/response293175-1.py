
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize a list to hold user data
users_data = []

# Loop through the pages with IDs from 1 to 100
for page_id in range(1, 101):
    url = f'https://example.com?id={page_id}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all users on the page
        users = soup.find_all('a')

        for user in users:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Append the user data to the list
            users_data.append({
                'Photo': user_photo,
                'Name': username,
                'Title': headline
            })

# Convert the data to a DataFrame
df = pd.DataFrame(users_data)

# Output to another site or save to CSV
df.to_csv('users_data.csv', index=False)
print("User data has been scraped and outputted to users_data.csv.")
