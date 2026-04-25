
import xml.etree.ElementTree as ET

# Sample soap response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the XML
soap_envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

soap_body = ET.SubElement(soap_envelope, "soap:Body")
response = ET.SubElement(soap_body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Iterate over the notifications and create XML elements
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = value

# Convert the ElementTree to a string
xml_string = ET.tostring(soap_envelope, encoding='unicode')

print(xml_string)
