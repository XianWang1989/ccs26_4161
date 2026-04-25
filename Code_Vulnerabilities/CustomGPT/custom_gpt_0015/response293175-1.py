
import requests
from bs4 import BeautifulSoup
import os

# Base URL of the site to crawl
base_url = "http://example.com?id={}"

# Directory to save images
if not os.path.exists('user_images'):
    os.makedirs('user_images')

# Function to crawl a given page
def crawl_page(page_id):
    url = base_url.format(page_id)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve page {page_id}")
        return None

# Function to extract user data
def extract_user_data(soup):
    users = []
    for user_section in soup.find_all('a'):
        img_tag = user_section.find('img')
        username_tag = user_section.find_next('h1', class_='username')
        headline_tag = username_tag.find_next('p', class_='headline') if username_tag else None

        if img_tag and username_tag and headline_tag:
            user_data = {
                'photo': img_tag['src'],
                'name': username_tag.text.strip(),
                'title': headline_tag.text.strip()
            }
            users.append(user_data)
    return users

# Main function to crawl multiple pages
def main():
    all_users = []
    for page_id in range(1, 101):
        print(f"Crawling page {page_id}...")
        soup = crawl_page(page_id)

        if soup:
            users = extract_user_data(soup)
            all_users.extend(users)
            for user in users:
                # Download images
                img_response = requests.get(user['photo'])
                img_name = os.path.join('user_images', user['name'].replace(" ", "_") + '.jpg')
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)

    print(f"Total users extracted: {len(all_users)}")

if __name__ == "__main__":
    main()
