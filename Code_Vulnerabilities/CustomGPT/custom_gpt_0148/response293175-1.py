
import requests
from bs4 import BeautifulSoup

base_url = 'http://example.com?id='
output_data = []

# Loop through pages 1 to 100
for page_id in range(1, 101):
    url = f"{base_url}{page_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find user entries on the page
        user_entries = soup.find_all('a')

        for entry in user_entries:
            photo = entry.find('img')['src']
            username = entry.find_next('h1', class_='username').text
            title = entry.find_next('p', class_='headline').text

            output_data.append({
                'photo': photo,
                'username': username,
                'title': title
            })
    else:
        print(f"Failed to retrieve page {page_id}")

# Output or save your data
for data in output_data:
    print(data)
