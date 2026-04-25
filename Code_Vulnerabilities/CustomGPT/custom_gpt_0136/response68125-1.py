
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True  # File exists
        else:
            return False  # File does not exist
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # An error occurred

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print(f"The file at {url} exists.")
else:
    print(f"The file at {url} does not exist.")
