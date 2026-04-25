
import requests
from bs4 import BeautifulSoup

# Function to crawl and extract data
def crawl_users(base_url, total_pages):
    users_data = []

    for i in range(1, total_pages + 1):
        # Create the URL for each page
        response = requests.get(f"{base_url}?id={i}")

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user containers
            user_containers = soup.find_all('a', href=True)

            # Loop through each user container and extract information
            for user in user_containers:
                img_tag = user.find('img')  # Find the img tag for user photo
                username = user.find_next('h1', class_='username').text  # Get username
                headline = user.find_next('p', class_='headline').text  # Get headline

                user_photo = img_tag['src'] if img_tag else None

                # Append extracted information to the users_data list
                users_data.append({
                    "photo": user_photo,
                    "name": username,
                    "title": headline
                })

    return users_data

# Base URL of the site you're crawling
base_url = "https://example.com"
total_pages = 100  # Total pages to crawl

# Call the function
users = crawl_users(base_url, total_pages)

# Print user data (or output it to another site as needed)
for user in users:
    print(user)
