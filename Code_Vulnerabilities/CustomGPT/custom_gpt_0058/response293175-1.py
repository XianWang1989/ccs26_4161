
import requests
from bs4 import BeautifulSoup

# Function to crawl and extract user information
def crawl_example_site():
    all_users = []

    for page_id in range(1, 101):  # Loop through page IDs 1 to 100
        url = f'https://example.com?id={page_id}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all user containers on the page
            user_containers = soup.find_all('a')
            for user in user_containers:
                user_photo = user.find('img')['src'] if user.find('img') else 'No image'
                username = user.find_next('h1', class_='username').text if user.find_next('h1', class_='username') else 'No name'
                title = user.find_next('p', class_='headline').text if user.find_next('p', class_='headline') else 'No title'

                all_users.append({
                    'photo': user_photo,
                    'name': username,
                    'title': title
                })
        else:
            print(f'Failed to retrieve page {page_id}')

    return all_users

# Function to output extracted data to another site (mockup function)
def output_to_site(users):
    for user in users:
        # Replace this with actual logic to post to another site
        print(f"User Photo: {user['photo']}, Name: {user['name']}, Title: {user['title']}")

# Main execution
if __name__ == "__main__":
    users_data = crawl_example_site()
    output_to_site(users_data)
