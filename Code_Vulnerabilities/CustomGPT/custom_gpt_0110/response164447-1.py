
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample raw response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the body
body = ET.SubElement(envelope, "soap:Body")

# Create the response element
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Create the result element
result = ET.SubElement(response, "GetNotificationsResult")

# Loop through notifications to create NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")

    # Add child elements
    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_elem, "Published")
    published_elem.text = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S").isoformat()

# Convert the tree to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

print(xml_string)
