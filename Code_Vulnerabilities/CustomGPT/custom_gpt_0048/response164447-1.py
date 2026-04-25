
import xml.etree.ElementTree as ET

# Sample input data from SOAP response
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the main Envelope structure
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add each NotificationData
for notification in notification_data:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        item = ET.SubElement(notification_element, key)
        item.text = str(value)

# Convert to a string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the result
print(xml_str)
