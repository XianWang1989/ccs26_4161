
import requests
from bs4 import BeautifulSoup

# URL template
base_url = "http://example.com?id={}"

# List to hold user data
users_data = []

# Loop through the pages
for page_id in range(1, 101):
    # Construct the URL for each page
    url = base_url.format(page_id)

    # Fetch the page
    response = requests.get(url)
    # Check for successful response
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user entries (assuming they are in a specific tag, adjust as needed)
        user_entries = soup.find_all('a', href=True)

        for entry in user_entries:
            user_photo = entry.find('img')['src']  # Extract user photo
            username = entry.find_next('h1', class_='username').text  # Extract username
            headline = entry.find_next('p', class_='headline').text  # Extract headline

            # Append user data to the list
            users_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output or save users_data to another site
for user in users_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
