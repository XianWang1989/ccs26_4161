
import xml.etree.ElementTree as ET

# Example data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2001-01-01T00:00:00"},
]

# Create SOAP Envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create Body
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        ET.SubElement(notification_element, key).text = str(value)

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_string)
