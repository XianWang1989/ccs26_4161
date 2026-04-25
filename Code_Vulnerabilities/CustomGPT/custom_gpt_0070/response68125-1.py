
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

url = 'http://hostname/directory/file.jpg'
if check_file_exists(url):
    print(f'The file exists at {url}')
else:
    print(f'The file does not exist at {url}')
