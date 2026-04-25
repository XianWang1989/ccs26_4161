
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to check existence without downloading
        return response.status_code == 200  # Check if the response is OK
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print(f"The file exists at {url}")
else:
    print(f"The file does not exist at {url}")
