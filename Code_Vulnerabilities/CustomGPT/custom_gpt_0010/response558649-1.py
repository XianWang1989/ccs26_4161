
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Example usage
url = 'https://api.example.com/data'
data = fetch_data(url)
print(data)
