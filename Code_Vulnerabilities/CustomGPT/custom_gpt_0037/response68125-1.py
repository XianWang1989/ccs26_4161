
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to check if the file exists without downloading it
        return response.status_code == 200  # HTTP 200 means the file exists
    except requests.RequestException as e:
        print(f"Error: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
