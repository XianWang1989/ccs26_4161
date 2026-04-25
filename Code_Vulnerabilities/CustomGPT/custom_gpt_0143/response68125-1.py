
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to check for existence without downloading content
        return response.status_code == 200  # File exists if status code is 200
    except requests.RequestException:
        return False  # If there's any error, file does not exist

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists!")
else:
    print("File does not exist.")
