
import requests

def file_exists(url):
    try:
        response = requests.head(url)
        # Check if the file exists by examining the status code
        return response.status_code == 200
    except requests.RequestException as e:
        # Handle any exceptions (e.g., network errors)
        print(f"Error checking file: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if file_exists(url):
    print(f"The file exists: {url}")
else:
    print(f"The file does not exist: {url}")
