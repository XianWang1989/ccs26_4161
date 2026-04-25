
import requests
from requests.exceptions import SSLError

url = "https://example.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    print(response.content)
except SSLError as ssl_err:
    print("SSL error occurred:", ssl_err)
except Exception as e:
    print("An error occurred:", e)
