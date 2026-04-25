
import requests

url = "http://hostname/directory/file.jpg"

try:
    response = requests.head(url)
    if response.status_code == 200:
        print("File exists.")
    else:
        print("File does not exist.")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
