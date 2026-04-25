
import xml.etree.ElementTree as ET

# Sample data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root elements
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {'xmlns': "http://localhost/WS.asmx"})
result = ET.SubElement(response, 'GetNotificationsResult')

# Add each notification to the XML
for notification in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notification_data, key)
        child.text = value if key != 'Published' else value.replace(" ", "T")

# Create a string representation of the XML
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the formatted XML string
print(xml_str)
