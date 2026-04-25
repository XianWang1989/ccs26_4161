
import requests

def check_requests():
    try:
        response = requests.get('https://www.example.com')
        if response.status_code == 200:
            print("Requests is working fine!")
        else:
            print(f"Received a response with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

check_requests()
