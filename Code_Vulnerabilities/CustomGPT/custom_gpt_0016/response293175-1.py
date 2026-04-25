
import requests
from bs4 import BeautifulSoup

# Base URL of the site to crawl
BASE_URL = "http://example.com?id={}"

# Function to crawl and extract user data
def crawl_users():
    users_data = []

    for i in range(1, 101):  # Looping through page IDs from 1 to 100
        response = requests.get(BASE_URL.format(i))

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            users = soup.find_all('a')  # Find all anchor tags

            for user in users:
                user_data = {}
                img_tag = user.find('img')  # Get the image tag
                if img_tag and 'src' in img_tag.attrs:
                    user_data['photo'] = img_tag['src']  # User photo URL

                username = user.find_next('h1', class_='username')
                headline = user.find_next('p', class_='headline')

                if username:
                    user_data['name'] = username.text.strip()  # User name
                if headline:
                    user_data['title'] = headline.text.strip()  # User title

                if user_data:
                    users_data.append(user_data)

    return users_data

# Call the function and print the results
if __name__ == "__main__":
    user_data = crawl_users()
    for user in user_data:
        print(user)
