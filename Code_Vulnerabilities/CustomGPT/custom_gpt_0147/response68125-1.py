
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check for 200 OK response
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
    print("File exists.")
else:
    print("File does not exist.")
