
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site
base_url = "https://example.com?id={}"

# Directory to save images
os.makedirs("user_images", exist_ok=True)

# Function to crawl a single page
def crawl_page(page_id):
    url = base_url.format(page_id)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all user entries on the page
    users = soup.find_all('a', href=True)

    for user in users:
        try:
            # Get user photo
            img_tag = user.find('img')
            img_url = img_tag['src'] if img_tag else None

            if img_url:
                img_response = requests.get(img_url)
                img_name = os.path.join("user_images", img_url.split("/")[-1])
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

            # Get username and headline
            username = user.find_next('h1', class_='username').text
            headline = user.find_next('p', class_='headline').text

            print(f"User: {username}, Title: {headline}, Image saved as: {img_name}")

        except Exception as e:
            print(f"Error processing user: {e}")

# Main function to crawl multiple pages
def main():
    for page_id in range(1, 101):  # From id=1 to id=100
        crawl_page(page_id)

if __name__ == "__main__":
    main()
