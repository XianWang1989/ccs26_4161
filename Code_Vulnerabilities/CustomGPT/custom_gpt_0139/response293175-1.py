
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
BASE_URL = "http://example.com?id={}"

def crawl_site():
    users_data = []

    # Loop through the pages with IDs 1 to 100
    for page_id in range(1, 101):
        response = requests.get(BASE_URL.format(page_id))

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Retrieve user elements
            users = soup.find_all('a', href=True)  # Find all links

            for user in users:
                if user.img:  # Check if there is an image
                    user_photo = user.img['src']
                    username = user.find_next('h1', class_='username').text.strip()
                    headline = user.find_next('p', class_='headline').text.strip()

                    users_data.append({
                        'photo': user_photo,
                        'name': username,
                        'title': headline,
                    })
        else:
            print(f"Failed to retrieve page {page_id}: {response.status_code}")

    return users_data

# Output the crawled user data
if __name__ == "__main__":
    user_info = crawl_site()
    for user in user_info:
        print(user)
