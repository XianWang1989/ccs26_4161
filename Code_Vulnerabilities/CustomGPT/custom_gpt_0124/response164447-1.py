
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response in a dictionary format
notifications = [
    {
        "Id": 1,
        "Title": "notification 1",
        "Message": "bla bla.",
        "Published": "2000-01-01 00:00:00"
    },
    {
        "Id": 2,
        "Title": "notification 2",
        "Message": "bla bla.",
        "Published": "2000-01-01 00:00:00"
    }
]

# Create the root of the SOAP Envelope
envelope = ET.Element(
    '{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
    {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
    }
)

body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result = ET.SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

# Add NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, '{http://localhost/WS.asmx}NotificationData')

    id_elem = ET.SubElement(notification_elem, 'Id')
    id_elem.text = str(notification['Id'])

    title_elem = ET.SubElement(notification_elem, 'Title')
    title_elem.text = notification['Title']

    message_elem = ET.SubElement(notification_elem, 'Message')
    message_elem.text = notification['Message']

    published_elem = ET.SubElement(notification_elem, 'Published')
    # Format date to ISO 8601
    published_date = datetime.strptime(notification['Published'], "%Y-%m-%d %H:%M:%S")
    published_elem.text = published_date.isoformat()

# Convert to string
xml_str = ET.tostring(envelope, encoding='unicode')
print(xml_str)
