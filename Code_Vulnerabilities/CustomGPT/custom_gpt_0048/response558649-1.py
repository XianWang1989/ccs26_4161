
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        print(response.json())  # Parse and print JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

url = "https://api.example.com/data"
fetch_data(url)
