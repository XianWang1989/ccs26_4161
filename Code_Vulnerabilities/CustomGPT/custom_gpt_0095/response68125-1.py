
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the status code indicates the file exists
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print("File exists!")
else:
    print("File does not exist.")
