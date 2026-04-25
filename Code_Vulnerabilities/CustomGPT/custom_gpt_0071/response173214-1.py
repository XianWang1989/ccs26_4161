
# Sample Python code
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200 if successful
