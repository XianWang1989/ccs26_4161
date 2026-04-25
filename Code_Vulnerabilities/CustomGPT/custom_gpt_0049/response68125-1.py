
import requests

def file_exists(url):
    try:
        response = requests.head(url)
        # If the status code is 200, the file exists
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if file_exists(url):
    print(f"The file exists: {url}")
else:
    print(f"The file does not exist: {url}")
