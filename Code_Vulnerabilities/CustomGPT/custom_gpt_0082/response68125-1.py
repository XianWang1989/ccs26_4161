
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the status code is 200 (OK), 404 (Not Found), etc.
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print("The file exists.")
else:
    print("The file does not exist.")
