
import xml.etree.ElementTree as ET

# Example input
notification_data = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
]

# Create the root structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})
body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})
result = ET.SubElement(response, 'GetNotificationsResult')

# Add NotificationData elements
for notification in notification_data:
    notification_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = str(value)

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode')

print(xml_string)
