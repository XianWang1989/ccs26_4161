
import xml.etree.ElementTree as ET

# Sample data extracted from SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the XML structure
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

for notification in notifications:
    notification_element = ET.SubElement(result, 'NotificationData')

    id_element = ET.SubElement(notification_element, 'Id')
    id_element.text = str(notification['Id'])

    title_element = ET.SubElement(notification_element, 'Title')
    title_element.text = notification['Title']

    message_element = ET.SubElement(notification_element, 'Message')
    message_element.text = notification['Message']

    published_element = ET.SubElement(notification_element, 'Published')
    published_element.text = notification['Published']

# Create a string representation of the XML
xml_string = ET.tostring(envelope, encoding='unicode')

print(xml_string)
