
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # Return True if the status code indicates the file exists
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file: {e}")
        return False

# Example usage
file_url = "http://hostname/directory/file.jpg"
if check_file_exists(file_url):
    print("File exists!")
else:
    print("File does not exist.")
