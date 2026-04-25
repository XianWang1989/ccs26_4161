
import xml.etree.ElementTree as ET

# Sample input string from SOAP response
response = """
(ArrayOfNotificationData){NotificationData[] = 
(NotificationData){Id = 1 Title = "notification 1" Message = "bla bla." Published = 2000-01-01 00:00:00}, 
(NotificationData){Id = 2 Title = "notification 2" Message = "bla bla." Published = 2000-01-01 00:00:00}
}
"""

# Function to parse the response and generate XML
def convert_to_xml(response):
    # Create root elements
    envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    response_elem = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
    result_elem = ET.SubElement(response_elem, "{http://localhost/WS.asmx}GetNotificationsResult")

    # Parse the response string
    notifications = response.strip().split("},")

    for notification in notifications:
        if notification.strip():
            # Extract Id, Title, Message, and Published
            parts = notification.split()
            id_ = parts[1].split('=')[1].strip()
            title = parts[2].split('=')[1].strip('"')
            message = parts[3].split('=')[1].strip('"')
            published = parts[4].split('=')[1].strip()

            # Create NotificationData element
            notification_data_elem = ET.SubElement(result_elem, "{http://localhost/WS.asmx}NotificationData")
            ET.SubElement(notification_data_elem, "Id").text = id_
            ET.SubElement(notification_data_elem, "Title").text = title
            ET.SubElement(notification_data_elem, "Message").text = message
            ET.SubElement(notification_data_elem, "Published").text = published

    # Convert to string
    return ET.tostring(envelope, encoding='unicode')

# Generate the XML
xml_output = convert_to_xml(response)
print(xml_output)
