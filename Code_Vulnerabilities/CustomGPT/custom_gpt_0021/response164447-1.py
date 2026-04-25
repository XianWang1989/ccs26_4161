
import xml.etree.ElementTree as ET

# Sample SOAP response
response = {
    "NotificationData": [
        {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
        {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    ]
}

def create_soap_response(data):
    # Create the root envelope
    envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')

    # Create the body element
    body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

    # Create the response for GetNotifications
    response_elem = ET.SubElement(body, 'GetNotificationsResponse', 
                                   xmlns="http://localhost/WS.asmx")
    result = ET.SubElement(response_elem, 'GetNotificationsResult')

    # Add NotificationData entries
    for notification in data['NotificationData']:
        notification_elem = ET.SubElement(result, 'NotificationData')
        ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
        ET.SubElement(notification_elem, 'Title').text = notification['Title']
        ET.SubElement(notification_elem, 'Message').text = notification['Message']
        ET.SubElement(notification_elem, 'Published').text = notification['Published'].replace(" ", "T")

    return ET.tostring(envelope, encoding='unicode')

# Convert current response to SOAP format
soap_response = create_soap_response(response)
print(soap_response)
