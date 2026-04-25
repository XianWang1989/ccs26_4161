
import xml.etree.ElementTree as ET

# Sample input data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the main structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Add notification data
for notification in notification_data:
    notification_element = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_element, "Id").text = str(notification["Id"])
    ET.SubElement(notification_element, "Title").text = notification["Title"]
    ET.SubElement(notification_element, "Message").text = notification["Message"]
    ET.SubElement(notification_element, "Published").text = notification["Published"].replace(" ", "T")

# Generate the string representation of the XML
xml_str = ET.tostring(envelope, encoding='unicode')
print(xml_str)
