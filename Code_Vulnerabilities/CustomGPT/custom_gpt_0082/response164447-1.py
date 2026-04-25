
import xml.etree.ElementTree as ET

# Sample data (mocking the SOAP response)
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root of the SOAP Envelope
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                       xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                       xmlns_xsd="http://www.w3.org/2001/XMLSchema")
body = ET.SubElement(envelope, "soap:Body")

# Create the GetNotificationsResponse element
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Populate NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_data, key)
        child.text = str(value)

# Convert the XML structure to a string
xml_str = ET.tostring(envelope, encoding='utf-8', method='xml').decode('utf-8')
print(xml_str)
