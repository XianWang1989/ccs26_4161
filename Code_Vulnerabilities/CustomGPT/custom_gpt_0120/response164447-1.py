
import xml.etree.ElementTree as ET

# Given data from the SOAP response
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
]

# Create the root elements
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", 
                         {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData to the result
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_element, key)
        child.text = str(value)

# Generate the XML string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_string)
