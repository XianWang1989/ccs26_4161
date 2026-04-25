
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
file_exists = check_file_exists(url)

if file_exists:
    print("File exists.")
else:
    print("File does not exist.")
