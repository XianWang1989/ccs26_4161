
import requests
from bs4 import BeautifulSoup

# Function to scrape user data from a page
def scrape_page(page_id):
    url = f"http://example.com?id={page_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        users = []

        # Find all user sections (modify this selector according to the actual HTML structure)
        user_cards = soup.find_all('div', class_='user-card')  # Replace 'user-card' with the actual class name of user containers

        for user_card in user_cards:
            photo = user_card.find('img')['src']  # Get user photo URL
            name = user_card.find('h1', class_='username').text  # User name
            title = user_card.find('p', class_='headline').text  # User title

            users.append({'photo': photo, 'name': name, 'title': title})

        return users
    else:
        print(f"Failed to retrieve page {page_id}")
        return []

# Main function to crawl multiple pages
def crawl_users():
    all_users = []
    for page_id in range(1, 101):  # From page 1 to 100
        users_on_page = scrape_page(page_id)
        all_users.extend(users_on_page)

    # Output the user data (you can modify this to output to another site)
    for user in all_users:
        print(user)

# Run the crawler
if __name__ == "__main__":
    crawl_users()
