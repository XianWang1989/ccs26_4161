
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data from your SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root of the XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add notification data
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")

    for key, value in notification.items():
        # Convert the Published date to the required format
        if key == "Published":
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat()
        child = ET.SubElement(notification_elem, key)
        child.text = str(value)

# Generate XML string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the resulting XML
print(xml_str)
