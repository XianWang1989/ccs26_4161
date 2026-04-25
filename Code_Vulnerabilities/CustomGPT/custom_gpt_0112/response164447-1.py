
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response
response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root elements for the SOAP message
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response_elem = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result_elem = ET.SubElement(response_elem, '{http://localhost/WS.asmx}GetNotificationsResult')

# Populate NotificationData from the SOAP response
for notification in response:
    notification_elem = ET.SubElement(result_elem, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = value if key != "Published" else datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat()

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the formatted XML
print(xml_str)
