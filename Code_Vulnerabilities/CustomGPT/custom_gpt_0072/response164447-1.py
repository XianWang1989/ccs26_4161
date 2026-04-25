
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data
response_data = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
]

# Create the root of the SOAP Envelope
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result = ET.SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

# Add NotificationData elements
for notification in response_data:
    notification_element = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_element, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_element, 'Title').text = notification['Title']
    ET.SubElement(notification_element, 'Message').text = notification['Message']
    published_dt = datetime.strptime(notification['Published'], "%Y-%m-%dT%H:%M:%S")
    ET.SubElement(notification_element, 'Published').text = published_dt.isoformat()

# Create the final XML string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

print(xml_str)
