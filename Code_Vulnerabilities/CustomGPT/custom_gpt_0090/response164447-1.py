
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create XML structure
soap_env = ET.Element("soap:Envelope", 
                      {"xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
                       "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                       "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"})
soap_body = ET.SubElement(soap_env, "soap:Body")
response = ET.SubElement(soap_body, "GetNotificationsResponse", 
                         {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Add each notification
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = value

# Convert to string
xml_str = ET.tostring(soap_env, encoding='unicode')
print(xml_str)
