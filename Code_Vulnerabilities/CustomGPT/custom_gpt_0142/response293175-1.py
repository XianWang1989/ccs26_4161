
import requests
from bs4 import BeautifulSoup

# Function to crawl user pages and extract data
def crawl_users(base_url, pages):
    user_data = []

    for page_id in range(1, pages + 1):
        # Construct the URL for the current page
        url = f"{base_url}?id={page_id}"
        print(f"Fetching data from: {url}")

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user entries
            user_entries = soup.find_all('a', href=True)

            for entry in user_entries:
                # Extract user photo
                img_tag = entry.find('img')
                img_src = img_tag['src'] if img_tag else None

                # Extract username and headline
                username_tag = entry.find_next('h1', class_='username')
                headline_tag = entry.find_next('p', class_='headline')

                username = username_tag.text.strip() if username_tag else "N/A"
                headline = headline_tag.text.strip() if headline_tag else "N/A"

                # Store the extracted data
                user_data.append({
                    'photo': img_src,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve page {page_id}: {response.status_code}")

    return user_data

# Define the base URL and number of pages
base_url = 'http://example.com'
total_pages = 100

# Crawl users and print extracted data
users = crawl_users(base_url, total_pages)
for user in users:
    print(user)
