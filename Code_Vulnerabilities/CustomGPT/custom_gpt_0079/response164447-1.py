
import xml.etree.ElementTree as ET

# Sample input data (as a string)
soap_response = """
(ArrayOfNotificationData){NotificationData[] = (NotificationData){Id = 1 Title = "notification 1" Message = "bla bla." Published = 2000-01-01 00:00:00}, (NotificationData){Id = 2 Title = "notification 2" Message = "bla bla." Published = 2000-01-01 00:00:00},}
"""

# Function to parse the response and generate XML
def convert_to_xml(response):
    # Parse the response to extract information
    notifications = []
    for line in response.split('},'):
        parts = line.strip().strip('()').split(' ')
        if len(parts) > 1:
            notification = {}
            for part in parts:
                if '=' in part:
                    key, value = part.split('=')
                    notification[key.strip()] = value.strip().strip('"')
            notifications.append(notification)

    # Create XML structure
    envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
    body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    response_element = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
    result = ET.SubElement(response_element, '{http://localhost/WS.asmx}GetNotificationsResult')

    for notification in notifications:
        notification_data = ET.SubElement(result, 'NotificationData')
        for key in ['Id', 'Title', 'Message', 'Published']:
            sub_element = ET.SubElement(notification_data, key)
            sub_element.text = notification[key]

    # Convert to string
    xml_str = ET.tostring(envelope, encoding='unicode')
    return xml_str

# Call the function and print the result
xml_output = convert_to_xml(soap_response)
print(xml_output)
