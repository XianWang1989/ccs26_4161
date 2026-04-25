
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"File exists: {url}")
            return True
        else:
            print(f"File does not exist: {url} (Status code: {response.status_code})")
            return False
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

# Example usage
file_url = "http://hostname/directory/file.jpg"
check_file_exists(file_url)
