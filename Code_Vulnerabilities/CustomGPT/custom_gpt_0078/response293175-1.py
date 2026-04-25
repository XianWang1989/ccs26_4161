
import requests
from bs4 import BeautifulSoup

def crawl_example_site(base_url, total_pages):
    users_data = []

    for page_id in range(1, total_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        users = soup.find_all('a')  # Assuming user info is in <a> tags

        for user in users:
            img_tag = user.find('img')
            if img_tag:
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

    return users_data


if __name__ == "__main__":
    base_url = "https://example.com"  # Replace with the actual base URL
    total_pages = 100  # Total number of pages to crawl
    data = crawl_example_site(base_url, total_pages)

    # Output the data (for example, printing or saving to a file)
    for user in data:
        print(user)
