
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the XML structure
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Append NotificationData elements
for notification in notifications:
    notif_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notif_elem, key)
        child.text = str(value)

# Convert the XML structure to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the resulting XML
print(xml_string)
