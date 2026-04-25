
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data from the SOAP response
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the main SOAP envelope and body
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Populate the XML with NotificationData
for notification in notification_data:
    notification_element = ET.SubElement(result, "NotificationData")

    id_element = ET.SubElement(notification_element, "Id")
    id_element.text = str(notification["Id"])

    title_element = ET.SubElement(notification_element, "Title")
    title_element.text = notification["Title"]

    message_element = ET.SubElement(notification_element, "Message")
    message_element.text = notification["Message"]

    published_element = ET.SubElement(notification_element, "Published")
    # Convert Published to the required format
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    published_element.text = published_date.isoformat()

# Convert the XML tree to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the XML string
print(xml_str)
