
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Check for successful response (status codes 200-399 indicate the file may exist)
        if response.status_code < 400:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = 'http://hostname/directory/file.jpg'
file_exists = check_file_exists(url)

if file_exists:
    print("File exists.")
else:
    print("File does not exist.")
