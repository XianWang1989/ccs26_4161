
import requests
from bs4 import BeautifulSoup
import threading

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.all_users = []

    def fetch_page(self, id):
        try:
            response = requests.get(f"{self.base_url}?id={id}", timeout=5)
            response.raise_for_status()  # Raise an error for bad status codes

            self.parse_users(response.content)
        except requests.RequestException as e:
            print(f"Error fetching page {id}: {e}")

    def parse_users(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        users = soup.find_all('a')

        for user in users:
            user_data = {}
            user_image = user.find('img')
            user_name = soup.find('h1', class_='username')
            user_title = soup.find('p', class_='headline')

            if user_image:
                user_data['photo'] = user_image['src']
            if user_name:
                user_data['name'] = user_name.text
            if user_title:
                user_data['title'] = user_title.text

            self.all_users.append(user_data)

    def run(self, start_id, end_id):
        threads = []
        for id in range(start_id, end_id + 1):
            thread = threading.Thread(target=self.fetch_page, args=(id,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return self.all_users

# Usage
base_url = "https://example.com"
crawler = Crawler(base_url)
user_data = crawler.run(1, 100)
print(user_data)
