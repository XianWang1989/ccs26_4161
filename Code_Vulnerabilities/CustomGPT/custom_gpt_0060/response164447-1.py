
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

# Sample SOAP response (the original format you provided)
soap_response = "(ArrayOfNotificationData){NotificationData[] = (NotificationData){Id = 1 Title = 'notification 1' Message = 'bla bla.' Published = '2000-01-01 00:00:00'}, (NotificationData){Id = 2 Title = 'notification 2' Message = 'bla bla.' Published = '2001-01-01 00:00:00'},}"

# Function to convert the soap response to desired XML format
def convert_soap_response(soap_response):
    # Extract NotificationData
    notifications = []
    # Extracting the data using a simple parser
    parts = soap_response.split("NotificationData{")[1:]  # Splitting to isolate each NotificationData
    for part in parts:
        part = part.split("}")[0]  # Get the content before the ending brace
        data = {}
        # Extracting Id, Title, Message, and Published
        for item in part.split(" "):
            if "=" in item:
                key, value = item.split("=", 1)
                data[key.strip()] = value.strip().strip('"').strip("'")
        notifications.append(data)

    # Creating the new XML structure
    envelope = Element('soap:Envelope', attrib={
            'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
            'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
            'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
        })

    body = SubElement(envelope, 'soap:Body')
    response = SubElement(body, 'GetNotificationsResponse', attrib={
        'xmlns': "http://localhost/WS.asmx"
    })
    result = SubElement(response, 'GetNotificationsResult')

    for notification in notifications:
        notification_elem = SubElement(result, 'NotificationData')
        for key, value in notification.items():
            element = SubElement(notification_elem, key)
            element.text = value

    # Convert XML to a pretty string
    xml_str = tostring(envelope, encoding='utf-8')
    pretty_xml = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="    ")

    return pretty_xml

# Convert and print the SOAP response as desired XML
xml_output = convert_soap_response(soap_response)
print(xml_output)
