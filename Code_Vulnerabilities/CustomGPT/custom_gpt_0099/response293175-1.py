
import requests
from bs4 import BeautifulSoup

# Function to crawl pages
def crawl_users(base_url, total_pages):
    user_data = []

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find user containers (modify as per actual HTML structure)
            users = soup.find_all('a', href=True)

            for user in users:
                # Get user photo
                photo_tag = user.find('img')
                user_photo = photo_tag['src'] if photo_tag else None

                # Get username
                username_tag = user.find_next('h1', class_='username')
                username = username_tag.text.strip() if username_tag else None

                # Get headline
                headline_tag = user.find_next('p', class_='headline')
                headline = headline_tag.text.strip() if headline_tag else None

                # Add user data to list
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'headline': headline
                })

    return user_data

# Main execution
if __name__ == "__main__":
    base_url = "http://example.com"  # Replace with the actual base URL
    total_pages = 100
    users_info = crawl_users(base_url, total_pages)

    # Output the collected data
    for user in users_info:
        print(f"Name: {user['name']}, Photo: {user['photo']}, Headline: {user['headline']}")
