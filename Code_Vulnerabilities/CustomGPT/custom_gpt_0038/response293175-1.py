
import requests
from bs4 import BeautifulSoup

def crawl_example_site(base_url, num_pages):
    users_data = []

    for page_id in range(1, num_pages + 1):
        url = f"{base_url}?id={page_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        users = soup.find_all('a')  # Find all anchor tags
        for user in users:
            img_tag = user.find('img')  # Get the image tag inside the anchor
            if img_tag:  # Check if img_tag exists
                user_photo = img_tag['src']
                username = user.find_next('h1', class_='username').text
                headline = user.find_next('p', class_='headline').text

                users_data.append({
                    'photo': user_photo,
                    'name': username,
                    'title': headline
                })

    return users_data

def output_to_another_site(data):
    output_url = 'https://your-output-site.com/api'  # Change this URL accordingly
    for user in data:
        response = requests.post(output_url, json=user)
        if response.status_code == 200:
            print(f"Uploaded: {user['name']}")
        else:
            print(f"Failed to upload: {user['name']}")

if __name__ == '__main__':
    base_url = 'https://example.com'
    num_pages = 100
    user_data = crawl_example_site(base_url, num_pages)
    output_to_another_site(user_data)
