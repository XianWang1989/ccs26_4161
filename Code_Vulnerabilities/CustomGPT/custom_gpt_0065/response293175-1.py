
import requests
from bs4 import BeautifulSoup

# Base URL template
base_url = "http://example.com?id={}"

# Function to scrape user data
def scrape_users(max_id):
    users_data = []

    for id in range(1, max_id + 1):
        # Fetch the page
        response = requests.get(base_url.format(id))
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        user_entries = soup.find_all('a', href=True)

        for entry in user_entries:
            # Get user photo, name, and title
            user_photo = entry.find('img')['src']
            username = entry.find_next_sibling('h1', class_='username').text
            headline = entry.find_next_sibling('p', class_='headline').text

            # Append user data to the list
            users_data.append({
                'photo': user_photo,
                'name': username,
                'title': headline
            })

    return users_data

# Main function to run the crawler
if __name__ == "__main__":
    max_id = 100
    users = scrape_users(max_id)

    # Output format (replace this with code to send data to another site)
    for user in users:
        print(f'<a href="{user["photo"]}"><img src="{user["photo"]}"></a>')
        print(f'<h1 class="username">{user["name"]}</h1>')
        print(f'<p class="headline">{user["title"]}</p>')
