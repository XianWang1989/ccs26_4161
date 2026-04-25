
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data from SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2001-01-01 00:00:00"}
]

# Create the root SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add NotificationData elements
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        if key == "Published":
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat()  # Format to ISO 8601
        ET.SubElement(notification_element, key).text = str(value)

# Convert to string
xml_str = ET.tostring(envelope, encoding='utf-8', method='xml').decode()
print(xml_str)
