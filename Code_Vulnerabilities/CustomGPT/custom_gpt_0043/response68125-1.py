
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response status code indicates that the file exists
        if response.status_code == 200:
            print(f"The file exists at: {url}")
            return True
        else:
            print(f"The file does not exist. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)
