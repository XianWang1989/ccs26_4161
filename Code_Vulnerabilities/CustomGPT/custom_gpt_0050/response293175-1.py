
import requests
from bs4 import BeautifulSoup

def crawl_users(base_url, total_pages):
    user_data = []

    for page_num in range(1, total_pages + 1):
        url = f"{base_url}?id={page_num}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            users = soup.find_all('a', href=True)
            for user in users:
                img_tag = user.find('img')
                name_tag = user.find_next('h1', class_='username')
                headline_tag = user.find_next('p', class_='headline')

                if img_tag and name_tag and headline_tag:
                    user_info = {
                        'photo': img_tag['src'],
                        'name': name_tag.text,
                        'title': headline_tag.text
                    }
                    user_data.append(user_info)

                    # Print or save the data as needed
                    print(user_info)  # Example output

        else:
            print(f"Failed to fetch page: {url}")

    return user_data

# Usage
base_url = "http://example.com"
total_pages = 100
crawl_users(base_url, total_pages)
