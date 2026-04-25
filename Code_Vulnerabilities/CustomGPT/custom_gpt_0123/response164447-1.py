
import xml.etree.ElementTree as ET

def convert_to_soap_xml(notification_data_list):
    # Create the root of the SOAP envelope
    envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

    response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
    result = ET.SubElement(response, "GetNotificationsResult")

    for notification in notification_data_list:
        notification_element = ET.SubElement(result, "NotificationData")

        id_elem = ET.SubElement(notification_element, "Id")
        id_elem.text = str(notification['Id'])

        title_elem = ET.SubElement(notification_element, "Title")
        title_elem.text = notification['Title']

        message_elem = ET.SubElement(notification_element, "Message")
        message_elem.text = notification['Message']

        published_elem = ET.SubElement(notification_element, "Published")
        published_elem.text = notification['Published']

    # Convert the entire structure to a string
    return ET.tostring(envelope, encoding='utf-8').decode('utf-8')

# Example notification data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Generate the SOAP XML
soap_xml = convert_to_soap_xml(notification_data)
print(soap_xml)
