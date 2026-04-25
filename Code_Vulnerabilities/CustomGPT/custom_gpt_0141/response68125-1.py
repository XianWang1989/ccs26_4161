
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response status code indicates that the file exists
        if response.status_code == 200:
            return True  # File exists
        elif response.status_code == 404:
            return False  # File not found
        else:
            print(f"Received unexpected status code: {response.status_code}")
            return False  # Handle other statuses as file not existing
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Handle exceptions, e.g., connection issues

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
