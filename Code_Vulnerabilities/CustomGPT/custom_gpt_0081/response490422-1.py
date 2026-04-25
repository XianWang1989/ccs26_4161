
# /opt/myPythonProject/mycode/my_script.py
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    url = "https://api.example.com/data"
    data = fetch_data(url)
    print(data)
