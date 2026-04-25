
import xml.etree.ElementTree as ET

# Sample input representing the SOAP response data
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'}
]

# Create the SOAP envelope
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope', {
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

# Create the SOAP body
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

# Create the GetNotificationsResponse
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})

# Create GetNotificationsResult
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_elem, 'Title').text = notification['Title']
    ET.SubElement(notification_elem, 'Message').text = notification['Message']
    ET.SubElement(notification_elem, 'Published').text = notification['Published']

# Convert the ElementTree to a string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode()
print(xml_str)
