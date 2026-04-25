
import requests
from bs4 import BeautifulSoup

# Base URL of the site you're crawling
base_url = "http://example.com?id="

# Placeholder for storing user data
user_data = []

# Loop through the required page IDs
for page_id in range(1, 101):  # From id=1 to id=100
    # Fetch the page content
    response = requests.get(base_url + str(page_id))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all relevant user sections
        users = soup.find_all('a', href=True)  # Finds all anchor tags (links)

        for user in users:
            # Extract user photo
            user_photo = user.find('img')['src'] if user.find('img') else None
            # Extract username from the sibling <h1> tag
            username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else None
            # Extract user title from the sibling <p> tag
            headline = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else None

            # Append the user's information to the list
            if user_photo and username and headline:
                user_data.append({
                    'photo': user_photo,
                    'username': username,
                    'headline': headline
                })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output the collected user data - here you may replace it with code to output to another site.
for user in user_data:
    print(user)  # For demonstration, print the user data
