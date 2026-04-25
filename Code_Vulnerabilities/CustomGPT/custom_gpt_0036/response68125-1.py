
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Sending a HEAD request to avoid downloading the file
        if response.status_code == 200:
            print(f"The file exists: {url}")
            return True
        elif response.status_code == 404:
            print(f"The file does not exist: {url}")
            return False
        else:
            print(f"Unexpected status code {response.status_code} for: {url}")
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
check_file_exists(url)
