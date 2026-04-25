
import xml.etree.ElementTree as ET
from datetime import datetime

# Example input data (parsed from your SOAP response)
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root elements for SOAP Envelope and Body
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add each notification to the Result
for notif in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notif["Id"])
    ET.SubElement(notification_elem, "Title").text = notif["Title"]
    ET.SubElement(notification_elem, "Message").text = notif["Message"]
    published_date = datetime.strptime(notif["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_elem, "Published").text = published_date.isoformat()

# Convert the XML structure to a string
xml_str = ET.tostring(envelope, encoding="unicode")

print(xml_str)
