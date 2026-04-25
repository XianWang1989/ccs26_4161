
from suds.client import Client
import xml.etree.ElementTree as ET

# Initialize the SOAP client
client = Client('http://localhost/WS.asmx?WSDL')

# Call the web service method to get notifications
response = client.service.GetNotifications()

# Example response format
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the XML structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response_elem = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
result_elem = ET.SubElement(response_elem, 'GetNotificationsResult')

# Add NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result_elem, 'NotificationData')
    for key, value in notification.items():
        elem = ET.SubElement(notification_elem, key)
        elem.text = str(value)

# Convert to string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print or return the XML string
print(xml_str)
