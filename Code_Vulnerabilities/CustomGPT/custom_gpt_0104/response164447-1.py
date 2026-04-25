
import xml.etree.ElementTree as ET

# Sample SOAP response as a list of dictionaries simulating your input
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
]

# Create the root element
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})

# Create the Body element
body = ET.SubElement(envelope, 'soap:Body')

# Create GetNotificationsResponse element
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})

# Create GetNotificationsResult element
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_elem, 'Title').text = notification['Title']
    ET.SubElement(notification_elem, 'Message').text = notification['Message']
    ET.SubElement(notification_elem, 'Published').text = notification['Published']

# Convert to a string
xml_string = ET.tostring(envelope, encoding='unicode')

# Output the generated XML
print(xml_string)
