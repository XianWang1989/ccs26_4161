
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # If the status code is 200, the file exists
        if response.status_code == 200:
            return True
        # If the status code is 404, the file does not exist
        elif response.status_code == 404:
            return False
        else:
            # For other status codes, return a message
            return f"File check returned status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)
print(f"Does the file exist? {file_exists}")
