
import requests

def does_file_exist(url):
    try:
        response = requests.head(url)
        # Check if the status code is 200 (OK)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if does_file_exist(url):
    print("File exists.")
else:
    print("File does not exist.")
