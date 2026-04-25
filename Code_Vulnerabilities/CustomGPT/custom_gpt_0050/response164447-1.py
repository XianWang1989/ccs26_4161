
import xml.etree.ElementTree as ET

# Sample SOAP response data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the main elements of the XML
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for data in notification_data:
    notification = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification, "Id").text = str(data["Id"])
    ET.SubElement(notification, "Title").text = data["Title"]
    ET.SubElement(notification, "Message").text = data["Message"]
    ET.SubElement(notification, "Published").text = data["Published"]

# Convert the XML tree to a string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Print the formatted XML
print(xml_str)
