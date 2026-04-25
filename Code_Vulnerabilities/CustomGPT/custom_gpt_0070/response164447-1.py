
import xml.etree.ElementTree as ET
from suds.client import Client

# Sample SOAP response (mocked for this example)
soap_response = {
    'NotificationData': [
        {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
        {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"}
    ]
}

# Create the XML structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
result = ET.SubElement(response, 'GetNotificationsResult')

# Add NotificationData items to the XML
for notification in soap_response['NotificationData']:
    notification_element = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_element, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_element, 'Title').text = notification['Title']
    ET.SubElement(notification_element, 'Message').text = notification['Message']
    ET.SubElement(notification_element, 'Published').text = notification['Published']

# Convert the ElementTree to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_string)
