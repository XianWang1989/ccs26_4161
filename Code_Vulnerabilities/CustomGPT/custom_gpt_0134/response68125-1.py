
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("The file exists.")
else:
    print("The file does not exist.")
