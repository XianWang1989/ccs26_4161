
import requests
from bs4 import BeautifulSoup

# Base URL for the site
base_url = "http://example.com?id={}"

# Loop through the pages
for page_id in range(1, 101):
    # Fetch the page content
    response = requests.get(base_url.format(page_id))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries
        user_entries = soup.find_all('a', href=True)  # Adjust selector based on actual HTML structure

        for entry in user_entries:
            # Extract user photo, name, and title
            img_tag = entry.find('img')
            header = entry.find_next('h1', class_='username')
            paragraph = header.find_next('p', class_='headline')

            user_photo = img_tag['src'] if img_tag else 'No photo'
            user_name = header.text if header else 'No name'
            user_title = paragraph.text if paragraph else 'No title'

            # Output or store the data as needed
            print(f"Photo: {user_photo}, Name: {user_name}, Title: {user_title}")

    else:
        print(f"Failed to retrieve page {page_id}, status code: {response.status_code}")
