import requests
from bs4 import BeautifulSoup
import os

base_url = "https://example.com?id="
output_data = []

# Create directory for downloaded images
os.makedirs("downloaded_images", exist_ok=True)

# Loop through pages 1 to 100
for page_id in range(1, 101):
    url = f"{base_url}{page_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_id}")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming each user block contains image, name, and title in a standard format
    user_blocks = soup.find_all("a", href=True)

    for a_tag in user_blocks:
        img_tag = a_tag.find("img")
        if not img_tag:
            continue

        # Find user info
        user_url = a_tag["href"]
        user_name_tag = soup.find("h1", class_="username")
        user_title_tag = soup.find("p", class_="headline")

        if user_name_tag and user_title_tag:
            user_name = user_name_tag.text.strip()
            user_title = user_title_tag.text.strip()
            photo_url = img_tag["src"]

            # Download the image
            photo_response = requests.get(photo_url)
            photo_filename = os.path.join("downloaded_images", os.path.basename(photo_url))
            with open(photo_filename, 'wb') as f:
                f.write(photo_response.content)

            # Save user data
            output_data.append({
                "name": user_name,
                "title": user_title,
                "photo": photo_filename,
                "profile_link": user_url
            })

# Output collected data
for user in output_data:
    print(f"Name: {user['name']}, Title: {user['title']}, Photo: {user['photo']}, Link: {user['profile_link']}")
