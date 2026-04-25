
import xml.etree.ElementTree as ET

# Example soap response
response_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root elements
envelope = ET.Element('soap:Envelope', xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")
body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Add NotificationData elements
for notification in response_data:
    notification_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        item = ET.SubElement(notification_elem, key)
        item.text = str(value)

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)
