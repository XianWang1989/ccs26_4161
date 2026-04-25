
import requests
from bs4 import BeautifulSoup

# Function to crawl pages and extract user data
def crawl_and_extract(base_url, total_pages):
    user_data = []

    # Loop through each page
    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user entries on the page
            users = soup.find_all('a', href=True)
            for user in users:
                # Ensure we check for the right structure
                img_tag = user.find('img')
                if img_tag:
                    user_photo = img_tag['src']
                    username = user.find_next('h1', class_='username').text
                    title = user.find_next('p', class_='headline').text

                    user_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': title
                    })
        else:
            print(f"Failed to retrieve page {page_id}")

    return user_data

if __name__ == "__main__":
    base_url = "http://example.com"
    total_pages = 100
    users_info = crawl_and_extract(base_url, total_pages)

    # Output the collected user data
    for user in users_info:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
