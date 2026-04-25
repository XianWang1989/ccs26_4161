
import requests
from bs4 import BeautifulSoup

# URL base
base_url = 'https://example.com?id='

# List to store user data
user_data = []

# Iterate through pages 1 to 100
for page_id in range(1, 101):
    # Construct the URL for the current page
    url = f"{base_url}{page_id}"

    # Send GET request to the URL
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract user elements
        user_elements = soup.find_all('a', href=True)

        for user in user_elements:
            user_photo = user.find('img')['src']
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            # Store the extracted data
            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })
    else:
        print(f"Failed to retrieve page {page_id}, status code: {response.status_code}")

# Output the collected user data
for user in user_data:
    print(f"User: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
