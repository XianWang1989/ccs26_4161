
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)  # Use HEAD to get header information
        return response.status_code == 200  # 200 indicates the file exists
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = 'http://hostname/directory/file.jpg'
if check_file_exists(url):
    print("File exists!")
else:
    print("File does not exist.")
