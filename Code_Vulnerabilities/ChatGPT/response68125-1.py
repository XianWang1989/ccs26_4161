
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD request to check for file existence
        # Check if the status code is in the 200 range
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("The file exists.")
else:
    print("The file does not exist.")
