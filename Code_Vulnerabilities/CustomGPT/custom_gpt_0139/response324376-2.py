
import requests

def send_post_request(url, data):
    try:
        # Make sure you're using the correct protocol (http or https) 
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.ConnectionError as e:
        # Log the error or handle it accordingly
        print(f"Connection Error: {e}")
    except requests.Timeout:
        print("Request timed out")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
