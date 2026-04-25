
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

url = 'http://hostname/directory/file.jpg'
file_exists = check_file_exists(url)

if file_exists:
    print(f"The file at {url} exists.")
else:
    print(f"The file at {url} does not exist.")
