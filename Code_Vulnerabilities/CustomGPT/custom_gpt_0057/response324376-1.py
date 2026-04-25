
import requests
from requests.packages.urllib3.util import connection

# Force IPv4
def allowed_gai_family():
    return socket.AF_INET

connection.allowed_gai_family = allowed_gai_family

response = requests.post('http://external.server/api', data={'key': 'value'})

print(response.status_code)
print(response.text)
