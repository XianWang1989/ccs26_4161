
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data structure
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
        "Published": "2001-01-01 00:00:00"
    }
]

# Create the SOAP Envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the Body
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})
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

    # Converting the date format
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_elem = ET.SubElement(notification_elem, "Published")
    published_elem.text = published_date.strftime("%Y-%m-%dT%H:%M:%S")

# Convert to string XML format (optional)
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode()
print(xml_str)
