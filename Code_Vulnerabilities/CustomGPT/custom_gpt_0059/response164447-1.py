
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data representing the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root elements
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
result = ET.SubElement(response, 'GetNotificationsResult')

# Iterate over notifications and create XML structure
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')

    for key, value in notification.items():
        # Format the Published date
        if key == "Published":
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat()

        child_elem = ET.SubElement(notification_elem, key)
        child_elem.text = str(value)

# Convert to string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_str)
