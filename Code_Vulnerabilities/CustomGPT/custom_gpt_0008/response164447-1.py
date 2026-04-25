
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data from SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create XML structure
soap_env = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
soap_body = ET.SubElement(soap_env, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

response = ET.SubElement(soap_body, 'GetNotificationsResponse', {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, 'GetNotificationsResult')

# Add NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_data, 'Title').text = notification['Title']
    ET.SubElement(notification_data, 'Message').text = notification['Message']
    # Format Published to the desired format
    published_time = datetime.strptime(notification['Published'], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_data, 'Published').text = published_time.isoformat()

# Generate the XML string
xml_string = ET.tostring(soap_env, encoding='unicode', method='xml')
print(xml_string)
