
import requests
from bs4 import BeautifulSoup

# Function to scrape user data from a page
def scrape_users(page_number):
    url = f"http://example.com?id={page_number}"
    response = requests.get(url)

    # If the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all user entries
        users = soup.find_all('a')  # Adjust selector based on actual HTML structure

        user_data = []

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
            else:
                user_photo = None

            username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else "No Name"
            headline = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else "No Title"

            user_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

        return user_data
    else:
        print(f"Failed to retrieve page {page_number}")
        return []

# Main script
all_users = []
for page in range(1, 101):  # Iterate through pages 1 to 100
    users_on_page = scrape_users(page)
    all_users.extend(users_on_page)

# Output the collected data
for user in all_users:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}")
