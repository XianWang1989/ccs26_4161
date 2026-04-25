
import xml.etree.ElementTree as ET

# Example soap response data
notifications = [
    {
        'Id': 1,
        'Title': 'notification 1',
        'Message': 'bla bla.',
        'Published': '2000-01-01T00:00:00'
    },
    {
        'Id': 2,
        'Title': 'notification 2',
        'Message': 'bla bla.',
        'Published': '2000-01-01T00:00:00'
    }
]

# Create the root elements of the XML
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Add each notification to the XML
for notification in notifications:
    notification_elem = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_elem, 'Title').text = notification['Title']
    ET.SubElement(notification_elem, 'Message').text = notification['Message']
    ET.SubElement(notification_elem, 'Published').text = notification['Published']

# Convert the XML tree to a string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the XML
print(xml_str)
