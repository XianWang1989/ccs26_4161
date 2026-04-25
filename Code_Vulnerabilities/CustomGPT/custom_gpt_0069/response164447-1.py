
import xml.etree.ElementTree as ET

# Mock SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root SOAP Envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

# Create GetNotificationsResponse
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add NotificationData for each notification
for notification in notifications:
    notification_data = ET.SubElement(result, "{http://localhost/WS.asmx}NotificationData")
    for key, value in notification.items():
        # Change Published format to ISO 8601
        if key == "Published":
            value = value.replace(" ", "T")
        child = ET.SubElement(notification_data, key)
        child.text = str(value)

# Convert to a string
xml_str = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Print the formatted XML
print(xml_str)
