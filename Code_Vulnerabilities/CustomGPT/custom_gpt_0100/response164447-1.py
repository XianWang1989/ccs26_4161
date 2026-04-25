
import xml.etree.ElementTree as ET

# Sample SOAP response data
data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root elements
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Populate the NotificationData elements
for item in data:
    notification = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification, "Id").text = str(item["Id"])
    ET.SubElement(notification, "Title").text = item["Title"]
    ET.SubElement(notification, "Message").text = item["Message"]
    ET.SubElement(notification, "Published").text = item["Published"]

# Convert to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the result
print(xml_str)
