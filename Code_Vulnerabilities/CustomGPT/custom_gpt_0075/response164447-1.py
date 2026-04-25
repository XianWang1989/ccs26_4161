
import re
import xml.etree.ElementTree as ET

def parse_soap_response(response):
    # Extract NotificationData using regex
    pattern = r'Id\s*=\s*(\d+)\s*Title\s*=\s*"([^"]+)"\s*Message\s*=\s*"([^"]+)"\s*Published\s*=\s*([\d-]+ [\d:]+)'
    notifications = re.findall(pattern, response)

    # Create the XML structure
    envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    response_elem = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
    result_elem = ET.SubElement(response_elem, "{http://localhost/WS.asmx}GetNotificationsResult")

    for notification in notifications:
        notification_elem = ET.SubElement(result_elem, "NotificationData")

        for i, tag in enumerate(["Id", "Title", "Message", "Published"]):
            child = ET.SubElement(notification_elem, tag)
            child.text = notification[i]

    # Convert the XML structure to a string
    return ET.tostring(envelope, encoding='unicode')

# Example usage
soap_response = '(ArrayOfNotificationData){NotificationData[] = (NotificationData){Id = 1 Title = "notification 1" Message = "bla bla." Published = 2000-01-01 00:00:00}, (NotificationData){Id = 2 Title = "notification 2" Message = "bla bla." Published = 2000-01-01 00:00:00},}'
xml_output = parse_soap_response(soap_response)
print(xml_output)
