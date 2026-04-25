
import xml.etree.ElementTree as ET

# Sample data extracted from the SOAP response
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
]

# Create the root elements
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})

result = ET.SubElement(response, 'GetNotificationsResult')

# Add notifications to the result
for notice in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notice['Id'])
    ET.SubElement(notification_data, 'Title').text = notice['Title']
    ET.SubElement(notification_data, 'Message').text = notice['Message']
    ET.SubElement(notification_data, 'Published').text = notice['Published']

# Convert the XML tree to a string
xml_string = ET.tostring(envelope, encoding='unicode')

print(xml_string)
