
import requests
from bs4 import BeautifulSoup

base_url = "https://example.com?id={}"
data = []

for page in range(1, 101):  # Loop through pages 1 to 100
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all user entries
        users = soup.find_all('a', href=True)  # Assuming user entries are in <a> tags

        for user in users:
            name = user.find_next('h1', class_='username').text.strip()
            title = user.find_next('p', class_='headline').text.strip()
            img_url = user.find('img')['src']  # Get the user photo URL

            data.append({
                'name': name,
                'title': title,
                'photo_url': img_url
            })

# Output the gathered data
for user in data:
    print(user)
