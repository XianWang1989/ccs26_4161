
import xml.etree.ElementTree as ET

# Sample data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the SOAP envelope
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {'xmlns': "http://localhost/WS.asmx"})
result = ET.SubElement(response, 'GetNotificationsResult')

# Add notifications to the result
for notification in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notification["Id"])
    ET.SubElement(notification_data, 'Title').text = notification["Title"]
    ET.SubElement(notification_data, 'Message').text = notification["Message"]
    ET.SubElement(notification_data, 'Published').text = notification["Published"]

# Convert to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the final XML
print(xml_str)

# Optionally, to pretty-print the XML
import xml.dom.minidom
print(xml.dom.minidom.parseString(xml_str).toprettyxml())
