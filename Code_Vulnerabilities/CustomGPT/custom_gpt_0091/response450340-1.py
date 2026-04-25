
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the config file
with open("new_config.xml", 'rb') as config_file:
    # Send the POST request with the XML data
    response = requests.post(url, data=config_file, headers={"Content-Type": "application/xml"})

# Print the response status code
print(response.status_code)
print(response.text)  # Optional: print the response body for debugging
