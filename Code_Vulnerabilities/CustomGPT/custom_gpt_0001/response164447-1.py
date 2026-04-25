
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data
response_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Populate the NotificationData
for notification in response_data:
    notification_elem = ET.SubElement(result, "NotificationData")
    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])
    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]
    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]
    published_elem = ET.SubElement(notification_elem, "Published")
    # Convert to the correct datetime format (ISO 8601)
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_elem.text = published_date.isoformat()

# Convert the XML structure to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the generated XML
print(xml_str)
