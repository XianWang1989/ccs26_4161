
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_request():
    url = "http://external-server.com/api"
    data = {"key": "value"}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Call the function
send_request()
