
import requests

def file_exists(url):
    try:
        response = requests.head(url)
        # Check if the response was successful
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
if file_exists(url):
    print("File exists.")
else:
    print("File does not exist.")
