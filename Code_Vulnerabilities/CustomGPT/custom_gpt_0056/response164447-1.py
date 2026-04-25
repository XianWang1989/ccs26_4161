
import xml.etree.ElementTree as ET

# Example SOAP response data
notifications = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"}
]

# Create the root of the SOAP XML
soap_env = ET.Element('soap:Envelope', xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/", 
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance", 
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")

# Create the Body
soap_body = ET.SubElement(soap_env, 'soap:Body')

# Create the response element
response = ET.SubElement(soap_body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Loop through notifications to create XML structure
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notification_elem, key)
        child.text = str(value)

# Convert the XML tree to a string
xml_str = ET.tostring(soap_env, encoding='unicode', method='xml')
print(xml_str)
