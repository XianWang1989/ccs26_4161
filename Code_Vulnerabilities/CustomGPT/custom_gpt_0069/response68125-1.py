
import requests

def file_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Example usage
url = 'http://hostname/directory/file.jpg'
if file_exists(url):
    print("The file exists!")
else:
    print("The file does not exist.")
