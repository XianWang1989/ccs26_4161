
import requests

url = "http://hostname/directory/file.jpg"

try:
    response = requests.head(url)
    if response.status_code == 200:
        print("File exists.")
    else:
        print("File does not exist. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
