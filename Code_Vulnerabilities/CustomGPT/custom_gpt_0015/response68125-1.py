
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response code is 200 (OK)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if check_file_exists(url):
    print("The file exists.")
else:
    print("The file does not exist.")
