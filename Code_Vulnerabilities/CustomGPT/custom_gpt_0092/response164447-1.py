
import xml.etree.ElementTree as ET

# Sample data from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add notifications to the result
for notification in notifications:
    notif_elem = ET.SubElement(result, "{http://localhost/WS.asmx}NotificationData")
    for key, value in notification.items():
        item_elem = ET.SubElement(notif_elem, key)
        item_elem.text = value

# Convert to a string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

print(xml_str)
