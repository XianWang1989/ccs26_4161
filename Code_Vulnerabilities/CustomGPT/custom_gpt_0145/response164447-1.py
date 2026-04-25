
import xml.etree.ElementTree as ET

# Simulated SOAP response array as a list of dictionaries
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2001-01-01T00:00:00"},
]

# Create the root 'soap:Envelope' element
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")

# Create 'soap:Body' element
body = ET.SubElement(envelope, "soap:Body")

# Create 'GetNotificationsResponse' element
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")

# Create 'GetNotificationsResult' element
result = ET.SubElement(response, "GetNotificationsResult")

# Loop through notifications and create 'NotificationData' elements
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    for key in notification:
        child = ET.SubElement(notification_elem, key)
        child.text = str(notification[key])

# Convert the ElementTree to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the XML string
print(xml_str)
