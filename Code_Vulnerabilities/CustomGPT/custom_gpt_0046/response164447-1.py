
import xml.etree.ElementTree as ET

def convert_to_soap_response(notification_data):
    # Create the SOAP Envelope
    envelope = ET.Element('soap:Envelope', {
        'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
    })

    # Create SOAP Body
    body = ET.SubElement(envelope, 'soap:Body')
    response = ET.SubElement(body, 'GetNotificationsResponse', {
        'xmlns': "http://localhost/WS.asmx"
    })

    result = ET.SubElement(response, 'GetNotificationsResult')

    # Add NotificationData elements
    for notification in notification_data:
        notification_elem = ET.SubElement(result, 'NotificationData')
        ET.SubElement(notification_elem, 'Id').text = str(notification['Id'])
        ET.SubElement(notification_elem, 'Title').text = notification['Title']
        ET.SubElement(notification_elem, 'Message').text = notification['Message']
        ET.SubElement(notification_elem, 'Published').text = notification['Published'].isoformat()

    # Convert to string
    return ET.tostring(envelope, encoding='unicode')

# Example notification data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Generate SOAP response
soap_response = convert_to_soap_response(notification_data)
print(soap_response)
