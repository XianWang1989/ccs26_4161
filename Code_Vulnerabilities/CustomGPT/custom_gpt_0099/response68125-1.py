
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Return True if the status code indicates that the file exists
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print("File exists.")
else:
    print("File does not exist.")
