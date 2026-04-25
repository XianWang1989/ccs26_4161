
import requests

def fetch_url(url):
    try:
        response = requests.get(url, verify=True)  # Ensure SSL verification
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    url = "https://www.example.com"
    content = fetch_url(url)
    print(content)
