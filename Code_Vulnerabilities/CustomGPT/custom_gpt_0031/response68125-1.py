
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if status code is 200 (OK) or 404 (Not Found)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            return False  # Handle other status codes if needed
    except requests.RequestException:
        return False  # Handle connection errors

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print("The file exists!")
else:
    print("The file does not exist.")
