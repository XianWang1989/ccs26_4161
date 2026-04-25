
import requests

def send_request():
    url = 'http://your-target-url.com/api'   # Replace with your target URL
    response = requests.post(url, data={'key': 'value'})  # Example POST request

    if response.status_code == 200:
        print('Request sent successfully')
    else:
        print(f'Error: {response.status_code} - {response.text}')

send_request()
