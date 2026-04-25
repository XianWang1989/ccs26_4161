
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # A 200 status code indicates the file exists
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print(f"The file at {url} exists.")
else:
    print(f"The file at {url} does not exist.")
