
import requests

def does_file_exist(url):
    try:
        response = requests.head(url)
        # Check if the status code indicates the file exists
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if does_file_exist(url):
    print("The file exists!")
else:
    print("The file does not exist.")
