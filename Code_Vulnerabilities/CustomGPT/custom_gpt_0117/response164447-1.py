
import xml.etree.ElementTree as ET
from datetime import datetime

# Example response from SOAP
response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root XML structure
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, "soap:Body")
response_elem = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})
result_elem = ET.SubElement(response_elem, "GetNotificationsResult")

# Add NotificationData elements
for notification in response:
    notification_elem = ET.SubElement(result_elem, "NotificationData")

    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_elem, "Published")
    # Format date to XML dateTime format
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_elem.text = published_date.isoformat()

# Convert the ElementTree to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the resulting XML
print(xml_string)
