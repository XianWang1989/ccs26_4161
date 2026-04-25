
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://example.com?id="

# Loop through the page IDs
for page_id in range(1, 101):  # From 1 to 100
    # Construct the full URL
    url = f"{base_url}{page_id}"

    # Send a GET request to the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user entries (assuming they have a common class or structure)
        users = soup.find_all('div', class_='user')  # Adjust this selector as needed

        for user in users:
            # Extract user photo, name, and title
            try:
                photo = user.find('img')['src']
                name = user.find('h1', class_='username').text.strip()
                title = user.find('p', class_='headline').text.strip()

                # Print or save the data as needed
                print(f"Name: {name}, Title: {title}, Photo URL: {photo}")

            except (AttributeError, TypeError):
                # Handle cases where the expected elements may not exist
                print("Missing user data.")
    else:
        print(f"Failed to retrieve page {page_id}: {response.status_code}")
