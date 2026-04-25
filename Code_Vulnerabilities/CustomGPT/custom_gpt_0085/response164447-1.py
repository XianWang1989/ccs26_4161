
import xml.etree.ElementTree as ET

# Sample data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the SOAP envelope
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {'xmlns': 'http://localhost/WS.asmx'})
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        elem = ET.SubElement(notification_data, key)
        elem.text = str(value)

# Convert the ElementTree to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Output the XML
print(xml_str)
