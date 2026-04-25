
import requests

def check_file_exists(url):
    try:
        response = requests.head(url)
        # If the response status code is 200, the file exists
        if response.status_code == 200:
            print("File exists.")
            return True
        else:
            print("File does not exist.")
            return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url = 'http://hostname/directory/file.jpg'
file_exists = check_file_exists(url)
