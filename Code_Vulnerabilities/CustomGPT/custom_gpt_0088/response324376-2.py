
import requests
import socket

# Function to send POST request
def send_post_request(data):
    # Set default to IPv4
    socket.setdefaultfamily(socket.AF_INET)

    try:
        response = requests.post('http://your-external-server.com/api', json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Process the response
    except requests.ConnectionError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data
data = {'key': 'value'}
send_post_request(data)
