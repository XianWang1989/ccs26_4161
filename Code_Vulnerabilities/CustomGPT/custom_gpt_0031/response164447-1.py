
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample soap response data (parsed)
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create SOAP Envelope
soap_ns = "http://schemas.xmlsoap.org/soap/envelope/"
response = ET.Element(f"{{{soap_ns}}}Envelope")
body = ET.SubElement(response, f"{{{soap_ns}}}Body")
get_notifications_response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
get_notifications_result = ET.SubElement(get_notifications_response, "GetNotificationsResult")

# Add NotificationData to the result
for notification in notifications:
    notification_data = ET.SubElement(get_notifications_result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]

    # Convert Published to the correct format
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_data, "Published").text = published_date.isoformat()

# Convert to string
xml_string = ET.tostring(response, encoding='unicode', method='xml')
print(xml_string)
