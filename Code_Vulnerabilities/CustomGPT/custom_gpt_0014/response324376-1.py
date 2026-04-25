
import requests
import socket

def send_post_request():
    # Force IPv4
    socket.setdefaultfamily(socket.AF_INET)

    try:
        response = requests.post('http://external-server/api/', data={'key': 'value'})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # or response.text, depending on your needs
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function in your view
send_post_request()
