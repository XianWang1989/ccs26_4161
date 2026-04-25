
import xml.etree.ElementTree as ET

# Example soap response as a string
soap_response = """
(ArrayOfNotificationData){NotificationData[] = (NotificationData){Id = 1 Title = "notification 1" Message = "bla bla." Published = 2000-01-01 00:00:00}, (NotificationData){Id = 2 Title = "notification 2" Message = "bla bla." Published = 2000-01-01 00:00:00},}
"""

# Parsing the response
def parse_response(response):
    notifications = []
    segments = response.split('(')[2:]  # Split and ignore the first two parts
    for segment in segments:
        if "NotificationData" in segment:
            parts = segment.split('}')
            for part in parts:
                if "Id" in part:
                    data = {}
                    fields = part.split(' ')
                    for field in fields:
                        if '=' in field:
                            key, value = field.split('=')
                            data[key.strip()] = value.strip().strip('"')
                    notifications.append(data)
    return notifications

# Building the SOAP XML
def build_soap_xml(notifications):
    envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
    result = ET.SubElement(response, "GetNotificationsResult")

    for notification in notifications:
        notification_elem = ET.SubElement(result, "NotificationData")
        for key, value in notification.items():
            child = ET.SubElement(notification_elem, key)
            child.text = value

    return ET.tostring(envelope, encoding='unicode')

# Extract notifications and build the XML
notifications = parse_response(soap_response)
soap_xml = build_soap_xml(notifications)

# Print the resulting SOAP XML
print(soap_xml)
