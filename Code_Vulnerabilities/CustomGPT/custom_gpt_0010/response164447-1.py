
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample data extracted from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root of the SOAP envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

# Create the GetNotificationsResponse element
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add each notification to the result
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]

    # Convert Published to the required format
    published_dt = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_elem, "Published").text = published_dt.isoformat()

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the resulting XML
print(xml_str)
