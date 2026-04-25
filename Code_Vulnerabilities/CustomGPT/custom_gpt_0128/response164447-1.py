
import xml.etree.ElementTree as ET

# Sample response
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the SOAP envelope
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, 'GetNotificationsResponse', 
                          xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notification_data:
    notification_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = str(value)

# Convert to a string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Print the generated XML
print(xml_str)
