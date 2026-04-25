
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # A successful response with status code 200 means the file exists
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("The file exists.")
else:
    print("The file does not exist.")
