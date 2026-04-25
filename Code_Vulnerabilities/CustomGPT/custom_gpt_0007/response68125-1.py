
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the status code indicates the file exists
        if response.status_code == 200:
            print(f"The file exists: {url}")
        else:
            print(f"The file does not exist. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
file_url = "http://hostname/directory/file.jpg"
check_file_exists(file_url)
