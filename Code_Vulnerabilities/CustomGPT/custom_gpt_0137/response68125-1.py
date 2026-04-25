
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to only fetch headers
        if response.status_code == 200:
            return True  # File exists
        else:
            return False  # File does not exist
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Any kind of error, considering file does not exist

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists!")
else:
    print("File does not exist.")
