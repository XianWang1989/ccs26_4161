
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import datetime

# Sample SOAP response
soap_response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the XML structure
envelope = Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})

body = SubElement(envelope, 'soap:Body')
response = SubElement(body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})
result = SubElement(response, 'GetNotificationsResult')

# Add NotificationData elements
for notification in soap_response:
    notification_data = SubElement(result, 'NotificationData')
    SubElement(notification_data, 'Id').text = str(notification['Id'])
    SubElement(notification_data, 'Title').text = notification['Title']
    SubElement(notification_data, 'Message').text = notification['Message']
    # Parse and format published date
    published_date = datetime.datetime.strptime(notification['Published'], '%Y-%m-%dT%H:%M:%S')
    SubElement(notification_data, 'Published').text = published_date.isoformat()

# Output the XML
xml_str = tostring(envelope, encoding='utf-8').decode('utf-8')
print(xml_str)
