
import xml.etree.ElementTree as ET

# Sample data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2001-01-01T00:00:00"},
]

# Create the XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", {
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]
    ET.SubElement(notification_data, "Published").text = notification["Published"]

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_string)
