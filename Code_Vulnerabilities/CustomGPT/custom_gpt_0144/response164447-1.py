from suds.client import Client
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Assuming WSDL URL
client = Client('http://localhost/WS.asmx?WSDL')
response = client.service.GetNotifications()

# Function to prettify XML
def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

# Build XML structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
})
body = ET.SubElement(envelope, 'soap:Body')
response_elem = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': 'http://localhost/WS.asmx'
})
result = ET.SubElement(response_elem, 'GetNotificationsResult')

# Iterate through notifications and build XML nodes
for notification in response:
    notif_elem = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notif_elem, 'Id').text = str(notification.Id)
    ET.SubElement(notif_elem, 'Title').text = notification.Title
    ET.SubElement(notif_elem, 'Message').text = notification.Message
    ET.SubElement(notif_elem, 'Published').text = notification.Published.strftime('%Y-%m-%dT%H:%M:%S')

# Output the XML string
print(prettify(envelope))
