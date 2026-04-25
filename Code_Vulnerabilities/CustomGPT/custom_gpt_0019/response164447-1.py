
import xml.etree.ElementTree as ET

# Example notification data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root elements for SOAP Envelope and Body
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Iterate through notifications and populate XML
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_element, key)
        child.text = str(value)

# Convert to a string representation of the XML
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

# Output the XML
print(xml_string)
