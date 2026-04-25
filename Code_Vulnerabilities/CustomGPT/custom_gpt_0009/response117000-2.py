
import requests

base_url = 'https://example.com/api/articles'
params = {'page': 1}
articles = []

while True:
    response = requests.get(base_url, params=params)
    data = response.json()

    if not data['articles']:  # Assuming an empty list means no more articles
        break

    articles.extend(data['articles'])
    params['page'] += 1

# Print all collected articles
for article in articles:
    print(f'Title: {article["title"]}')
    print(f'Link: {article["link"]}')
    print('-' * 40)
