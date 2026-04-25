
import xml.etree.ElementTree as ET

# Sample SOAP response string
soap_response = """
NotificationData[] = (NotificationData){Id = 1 Title = "notification 1" Message = "bla bla." Published = 2000-01-01 00:00:00}, 
(NotificationData){Id = 2 Title = "notification 2" Message = "bla bla." Published = 2000-01-01 00:00:00}
"""

# Parsing the SOAP response
notifications = []
for line in soap_response.splitlines():
    line = line.strip()
    if line.startswith("NotificationData"):
        parts = line.split("Id = ")[1:]  # Split and ignore anything before first Id
        for part in parts:
            notification = {}
            id_part, rest = part.split(" Title = ", 1)
            notification['Id'] = id_part.strip()
            title_part, rest = rest.split(" Message = ", 1)
            notification['Title'] = title_part.strip().strip('"')
            message_part, published_part = rest.split(" Published = ", 1)
            notification['Message'] = message_part.strip().strip('"')
            notification['Published'] = published_part.strip().replace(" ", "T")  # Fix the format
            notifications.append(notification)

# Constructing the SOAP XML response
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result = ET.SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

for notification in notifications:
    notification_elem = ET.SubElement(result, '{http://localhost/WS.asmx}NotificationData')
    for key, value in notification.items():
        item_elem = ET.SubElement(notification_elem, '{http://localhost/WS.asmx}' + key)
        item_elem.text = value

# Convert the ElementTree to a string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the output
print(xml_str)
