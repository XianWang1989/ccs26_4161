
import requests
import socket

# Force requests to use IPv4
def force_ipv4(host):
    fam = socket.AF_INET
    address_info = socket.getaddrinfo(host, None, fam)
    return address_info[0][4]

def send_post_request(url, data):
    # Get the IPv4 address
    ipv4_address = force_ipv4('your-external-server.com')

    # Send the POST request using the resolved IPv4 address
    response = requests.post(url, data=data, headers={'Host': ipv4_address})
    return response

# Example usage
url = "http://your-external-server.com/api"
data = {'key': 'value'}
response = send_post_request(url, data)

print(response.status_code, response.content)
