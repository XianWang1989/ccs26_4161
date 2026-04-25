
from suds.client import Client

# Replace with your actual WSDL URL
wsdl_url = 'http://localhost/WS.asmx?WSDL'
client = Client(wsdl_url)

# Example call to the service; replace with your actual method.
response = client.service.GetNotifications()
# This would then allow you to process the 'response' similar to the notification_data used above.
