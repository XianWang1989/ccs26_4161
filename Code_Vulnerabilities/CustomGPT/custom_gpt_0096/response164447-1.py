
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data extracted from the SOAP response
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
]

# Create the root of the SOAP Envelope
Envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})

# Create the Body element
Body = ET.SubElement(Envelope, 'soap:Body')
Response = ET.SubElement(Body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})
Result = ET.SubElement(Response, 'GetNotificationsResult')

# Iterate over the notifications and create XML elements
for notification in notifications:
    NotificationData = ET.SubElement(Result, 'NotificationData')

    # Add child elements for each attribute
    ET.SubElement(NotificationData, 'Id').text = str(notification['Id'])
    ET.SubElement(NotificationData, 'Title').text = notification['Title']
    ET.SubElement(NotificationData, 'Message').text = notification['Message']

    # Convert the Published date to the required format
    published_date = datetime.strptime(notification['Published'], '%Y-%m-%d %H:%M:%S')
    ET.SubElement(NotificationData, 'Published').text = published_date.isoformat()

# Convert the XML tree to a string
xml_str = ET.tostring(Envelope, encoding='utf-8').decode('utf-8')
print(xml_str)
