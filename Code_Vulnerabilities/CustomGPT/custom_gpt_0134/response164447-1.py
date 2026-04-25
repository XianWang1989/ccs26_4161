
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data
soap_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root of the XML structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Populate the XML with NotificationData
for notification in soap_data:
    notification_element = ET.SubElement(result, "NotificationData")

    id_element = ET.SubElement(notification_element, "Id")
    id_element.text = str(notification["Id"])

    title_element = ET.SubElement(notification_element, "Title")
    title_element.text = notification["Title"]

    message_element = ET.SubElement(notification_element, "Message")
    message_element.text = notification["Message"]

    published_element = ET.SubElement(notification_element, "Published")
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_element.text = published_date.isoformat()

# Convert to a string
xml_str = ET.tostring(envelope, encoding='unicode')

print(xml_str)
