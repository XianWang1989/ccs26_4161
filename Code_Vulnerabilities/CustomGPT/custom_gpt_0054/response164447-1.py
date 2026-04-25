
import xml.etree.ElementTree as ET

def convert_to_soap_xml(notifications):
    # Create the SOAP Envelope
    envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    response = ET.SubElement(body, "GetNotificationsResponse", 
                              xmlns="http://localhost/WS.asmx")
    result = ET.SubElement(response, "GetNotificationsResult")

    # Iterate through the notifications and create XML elements
    for notification in notifications:
        notification_elem = ET.SubElement(result, "NotificationData")

        id_elem = ET.SubElement(notification_elem, "Id")
        id_elem.text = str(notification['Id'])

        title_elem = ET.SubElement(notification_elem, "Title")
        title_elem.text = notification['Title']

        message_elem = ET.SubElement(notification_elem, "Message")
        message_elem.text = notification['Message']

        published_elem = ET.SubElement(notification_elem, "Published")
        published_elem.text = notification['Published'].isoformat()  # Use isoformat() for proper date-time

    # Convert the tree to a string
    return ET.tostring(envelope, encoding='unicode', method='xml')

# Sample input based on provided SOAP response
notifications_data = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
]

# Convert to SOAP XML
soap_xml = convert_to_soap_xml(notifications_data)
print(soap_xml)
