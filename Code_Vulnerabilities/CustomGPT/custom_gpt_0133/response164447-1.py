
import xml.etree.ElementTree as ET
from datetime import datetime

# Example SOAP response data structure
response_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

# Create GetNotificationsResponse
response = ET.SubElement(body, "GetNotificationsResponse", 
                         xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Populate NotificationData elements
for notification in response_data:
    notification_elem = ET.SubElement(result, "NotificationData")

    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_elem, "Published")
    # Convert published date to the desired format
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_elem.text = published_date.isoformat()

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode')

# Output the result
print(xml_str)
