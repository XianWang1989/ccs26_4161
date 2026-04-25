
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
