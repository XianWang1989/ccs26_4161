
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response in a structured format (simulated)
notifications = [
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

# Create the root SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Iterate over notifications and create XML elements
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")

    id_elem = ET.SubElement(notification_data, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_data, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_data, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_data, "Published")
    published_elem.text = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S").isoformat()

# Generate the final XML string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_str)
