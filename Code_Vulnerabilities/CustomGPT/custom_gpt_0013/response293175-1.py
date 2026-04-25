
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "http://example.com?id={}"

# Function to crawl user data
def crawl_users(start_id, end_id):
    user_data = []

    for page_id in range(start_id, end_id + 1):
        response = requests.get(base_url.format(page_id))
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries in the page
        users = soup.find_all('a', href=True)

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                img_src = img_tag['src']
                username = user.find_next_sibling('h1', class_='username').text
                headline = user.find_next_sibling('p', class_='headline').text

                # Store user info
                user_info = {
                    'photo': img_src,
                    'name': username,
                    'title': headline
                }
                user_data.append(user_info)

    return user_data

# Example usage
if __name__ == "__main__":
    start_id = 1
    end_id = 100
    users_info = crawl_users(start_id, end_id)

    # Output results (e.g., save to a file, or output to another site)
    for user in users_info:
        print(user)
