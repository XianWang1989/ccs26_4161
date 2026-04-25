
import requests

# Example function to fetch data using GET request
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Return JSON data if the response is valid
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Usage
data = fetch_data('https://api.example.com/data')
print(data)
