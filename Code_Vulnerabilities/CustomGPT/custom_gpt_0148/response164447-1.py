
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import datetime

# Sample soap response representation
response_data = {
    'NotificationData': [
        {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
        {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2000-01-01 00:00:00'},
    ]
}

# Create XML structure
soap_env = Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
soap_body = SubElement(soap_env, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = SubElement(soap_body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result = SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

# Add NotificationData elements
for notification in response_data['NotificationData']:
    notification_elem = SubElement(result, '{http://localhost/WS.asmx}NotificationData')

    id_elem = SubElement(notification_elem, 'Id')
    id_elem.text = str(notification['Id'])

    title_elem = SubElement(notification_elem, 'Title')
    title_elem.text = notification['Title']

    message_elem = SubElement(notification_elem, 'Message')
    message_elem.text = notification['Message']

    published_elem = SubElement(notification_elem, 'Published')
    published_date = datetime.datetime.strptime(notification['Published'], '%Y-%m-%d %H:%M:%S')
    published_elem.text = published_date.isoformat()  # Converts to `YYYY-MM-DDTHH:MM:SS`

# Convert to XML string
xml_str = tostring(soap_env, encoding='unicode')

# Print the resulting XML
print(xml_str)
