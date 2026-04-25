
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

# Function to create XML from the notification data
def create_soap_response(notifications):
    # Create the root elements
    envelope = Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
    body = SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    response = SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
    result = SubElement(response, 'GetNotificationsResult')

    # Add notification data to the result
    for notification in notifications:
        notification_data = SubElement(result, 'NotificationData')
        SubElement(notification_data, 'Id').text = str(notification['Id'])
        SubElement(notification_data, 'Title').text = notification['Title']
        SubElement(notification_data, 'Message').text = notification['Message']
        SubElement(notification_data, 'Published').text = notification['Published'].isoformat()

    # Convert to a pretty-printed XML string
    xml_str = tostring(envelope)
    pretty_xml = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
    return pretty_xml

# Example notification data
notifications = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2001-01-01T00:00:00'},
]

# Create and print the SOAP response
soap_response = create_soap_response(notifications)
print(soap_response)
