
from suds.client import Client
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Sample SOAP response
soap_response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create SOAP XML structure
envelope = Element('soap:Envelope', xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/")
body = SubElement(envelope, 'soap:Body')
response = SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = SubElement(response, 'GetNotificationsResult')

for notification in soap_response:
    notification_data = SubElement(result, 'NotificationData')
    SubElement(notification_data, 'Id').text = str(notification['Id'])
    SubElement(notification_data, 'Title').text = notification['Title']
    SubElement(notification_data, 'Message').text = notification['Message']
    SubElement(notification_data, 'Published').text = notification['Published']

# Convert XML to string
xml_str = tostring(envelope, encoding='unicode')

# Output XML
print(xml_str)
