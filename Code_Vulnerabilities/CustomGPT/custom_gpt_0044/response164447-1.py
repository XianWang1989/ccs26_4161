
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data
response_data = [
    {
        "Id": 1,
        "Title": "notification 1",
        "Message": "bla bla.",
        "Published": "2000-01-01 00:00:00"
    },
    {
        "Id": 2,
        "Title": "notification 2",
        "Message": "bla bla.",
        "Published": "2000-01-01 00:00:00"
    }
]

# Create XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add NotificationData elements
for notification in response_data:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    published_datetime = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_elem, "Published").text = published_datetime.isoformat()

# Convert to string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

print(xml_str)
