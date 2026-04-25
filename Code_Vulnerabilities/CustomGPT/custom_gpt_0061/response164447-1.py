
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Construct NotificationData entries
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")

    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_elem, "Published")
    published_elem.text = notification["Published"]

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print the XML
print(xml_string)
