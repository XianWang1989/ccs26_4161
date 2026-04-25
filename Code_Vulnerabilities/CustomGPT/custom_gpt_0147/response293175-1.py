
import requests
from bs4 import BeautifulSoup

def crawl_user_data():
    user_data = []

    # Loop through the range of pages
    for page_id in range(1, 101):
        url = f"http://example.com?id={page_id}"

        # Send HTTP GET request
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all user entries
            users = soup.find_all('a', href=True)  # Adjust based on the actual HTML structure

            for user in users:
                user_photo = user.find('img')['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                # Append the user data to the list
                user_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })
        else:
            print(f"Failed to retrieve page {page_id}")

    # Output the collected user data
    output_user_data(user_data)

def output_user_data(data):
    # Implement this function to send data to the another site
    for user in data:
        print(f"Name: {user['name']}, Title: {user['title']}, Photo URL: {user['photo']}")
        # You can use requests.post() to send this data to another site here.

# Start the crawling process
crawl_user_data()
