import requests
import socket

def post_request(url, data):
    response = requests.post(
        url,
        data=data,
        headers={'Content-Type': 'application/json'},
        # Force IPv4
        allow_redirects=True,
        timeout=10,
        stream=False,
        verify=True,
        cert=None,
        proxies=None,
        hooks=None,
        params=None,
        auth=None,
        cookies=None,
        files=None,
        json=None,
        headers=None,
        data=None,
        hooks=None,
        adapter_kwargs={'family': socket.AF_INET}
    )
    return response
