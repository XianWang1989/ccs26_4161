
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an error for HTTP errors
        return response.json()
    except requests.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.Timeout as e:
        print(f"Timeout error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
