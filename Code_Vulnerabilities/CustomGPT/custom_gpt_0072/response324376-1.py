
import requests

def send_post_request(url, data):
    # Force the connection to use IPv4
    proxies = {
        "http": "http://127.0.0.1:80",
        "https": "http://127.0.0.1:443",
    }
    response = requests.post(url, data=data, proxies=proxies)
    return response
