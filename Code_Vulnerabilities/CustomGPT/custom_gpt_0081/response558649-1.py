
import requests

# Example function to make a GET request
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Example usage
url = 'https://api.github.com/users/octocat'
data = fetch_data(url)
print(data)
