
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response status code indicates presence
        if response.status_code == 200:
            return True  # File exists
        elif response.status_code == 404:
            return False  # File does not exist
        else:
            return False  # Some other response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
