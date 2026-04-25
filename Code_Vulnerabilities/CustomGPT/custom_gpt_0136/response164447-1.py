
import xml.etree.ElementTree as ET

# Sample data representing the parsed SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Fill in NotificationData elements
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_element, "Id").text = str(notification["Id"])
    ET.SubElement(notification_element, "Title").text = notification["Title"]
    ET.SubElement(notification_element, "Message").text = notification["Message"]
    ET.SubElement(notification_element, "Published").text = notification["Published"]

# Convert to a string
xml_str = ET.tostring(envelope, encoding='unicode')
print(xml_str)
