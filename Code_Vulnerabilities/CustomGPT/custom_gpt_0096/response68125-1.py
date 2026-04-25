
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the status code is 200 (OK), which means the file exists
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking file: {e}")
        return False

file_url = "http://hostname/directory/file.jpg"
if check_file_exists(file_url):
    print("File exists!")
else:
    print("File does not exist.")
