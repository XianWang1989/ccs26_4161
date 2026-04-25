
import xml.etree.ElementTree as ET

# Original soap response data (simplified for the example)
notification_data_array = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
]

# Create the root XML structure
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

# Add NotificationData elements
for notification in notification_data_array:
    notification_elem = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_elem, 'Title').text = notification['Title']
    ET.SubElement(notification_elem, 'Message').text = notification['Message']
    ET.SubElement(notification_elem, 'Published').text = notification['Published'].replace(" ", "T")  # format to match required format

# Generate the final XML string
xml_bytes = ET.tostring(envelope, encoding='utf-8', method='xml')
xml_str = xml_bytes.decode('utf-8')

# Print the resulting XML
print(xml_str)
