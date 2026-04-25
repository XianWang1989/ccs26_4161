
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the status code indicates file existence
        if response.status_code == 200:
            print(f"The file exists: {url}")
            return True
        else:
            print(f"The file does not exist. Status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
file_url = "http://hostname/directory/file.jpg"
check_file_exists(file_url)
