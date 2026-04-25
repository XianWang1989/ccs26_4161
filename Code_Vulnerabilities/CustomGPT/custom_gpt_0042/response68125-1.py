
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response status code indicates the file exists
        if response.status_code == 200:
            print("File exists.")
            return True
        else:
            print("File does not exist.")
            return False
    except requests.RequestException as e:
        print(f"Error checking file: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
check_file_exists(url)
