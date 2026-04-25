
import requests

# Force IPv4
response = requests.get("http://<your_ip>", headers={"Host": "<your_host_ip>"})
