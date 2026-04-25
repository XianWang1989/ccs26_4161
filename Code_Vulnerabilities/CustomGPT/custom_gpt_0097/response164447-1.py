
import xml.etree.ElementTree as ET

# Your input data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the SOAP Envelope Structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add notification data to the result
for notify in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notify["Id"])
    ET.SubElement(notification_data, "Title").text = notify["Title"]
    ET.SubElement(notification_data, "Message").text = notify["Message"]
    ET.SubElement(notification_data, "Published").text = notify["Published"]

# Convert to a string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)
