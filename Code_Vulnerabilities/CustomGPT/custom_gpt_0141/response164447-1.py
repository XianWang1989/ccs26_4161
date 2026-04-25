
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample input representing the SOAP response in a structured format (as Python objects)
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
        "Published": "2001-01-01 00:00:00"
    }
]

# Create the root of the XML structure
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the SOAP body
body = ET.SubElement(envelope, "soap:Body")

# Create the GetNotificationsResponse element
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Create the GetNotificationsResult element
result = ET.SubElement(response, "GetNotificationsResult")

# Iterate through notifications and add them to XML
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")

    # Add each field as a child element
    for key, value in notification.items():
        # Format Published date to ISO format if necessary
        if key == "Published":
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat()

        child = ET.SubElement(notification_elem, key)
        child.text = str(value)

# Convert the XML structure to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the resulting XML
print(xml_str)
