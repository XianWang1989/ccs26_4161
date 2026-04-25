
import requests

def file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD request to fetch headers only
        return response.status_code == 200  # File exists if status code is 200
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

url = "http://hostname/directory/file.jpg"
if file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
