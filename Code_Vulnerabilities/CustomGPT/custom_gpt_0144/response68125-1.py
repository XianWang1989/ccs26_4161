import requests

def check_file_exists(url):
    try:
        # Send a HEAD request to check if the file exists
        response = requests.head(url)
        
        # If status code is 200, the file exists
        if response.status_code == 200:
            print(f"File exists: {url}")
            return True
        elif response.status_code == 404:
            print(f"File does not exist: {url}")
            return False
        else:
            print(f"Received unexpected status code {response.status_code} for {url}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while checking file: {e}")
        return False

# Example usage
url = "http://hostname/directory/file.jpg"
check_file_exists(url)
