
import requests

def file_exists(url):
    try:
        response = requests.head(url)
        # Check for status code 200 (OK)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if file_exists(url):
    print(f"The file exists at: {url}")
else:
    print(f"The file does not exist at: {url}")
