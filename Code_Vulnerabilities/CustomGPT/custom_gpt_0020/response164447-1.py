
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

# Sample data resembling the SOAP response
notification_data = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
]

# Create the XML structure
envelope = Element('soap:Envelope', xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                                     xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                                     xmlns_xsd="http://www.w3.org/2001/XMLSchema")
body = SubElement(envelope, 'soap:Body')
response = SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = SubElement(response, 'GetNotificationsResult')

for notification in notification_data:
    notification_elem = SubElement(result, 'NotificationData')
    SubElement(notification_elem, 'Id').text = str(notification['Id'])
    SubElement(notification_elem, 'Title').text = notification['Title']
    SubElement(notification_elem, 'Message').text = notification['Message']
    SubElement(notification_elem, 'Published').text = notification['Published']

# Generate the XML string
xml_str = tostring(envelope)
pretty_xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml()

print(pretty_xml_str)
