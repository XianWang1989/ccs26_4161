
import xml.etree.ElementTree as ET
from datetime import datetime

# Mocked SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData items
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_data, "Published").text = published_date.isoformat()

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print the final XML
print(xml_string)
