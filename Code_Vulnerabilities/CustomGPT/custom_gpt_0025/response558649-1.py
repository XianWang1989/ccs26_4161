
import ssl
import requests

# Create an SSL context
context = ssl.create_default_context()

# Make a HTTPS request with custom context
response = requests.get('https://example.com', verify=True, trust_env=False, timeout=10, ssl_context=context)
print(response.text)
