
import xml.etree.ElementTree as ET

# Sample input data (representing the parsed SOAP response)
notifications = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
]

# Create the root of the SOAP envelope
envelope = ET.Element('soap:Envelope', xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance", 
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Add NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child_elem = ET.SubElement(notification_elem, key)
        child_elem.text = str(value)

# Create the XML string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Print the XML output
print(xml_str)
