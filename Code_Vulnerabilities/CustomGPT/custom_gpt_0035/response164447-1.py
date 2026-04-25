
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample response data extracted from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Creating the XML structure
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")

body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

for notif in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notif["Id"])
    ET.SubElement(notification_elem, "Title").text = notif["Title"]
    ET.SubElement(notification_elem, "Message").text = notif["Message"]
    published_time = datetime.strptime(notif["Published"], "%Y-%m-%d %H:%M:%S").isoformat()
    ET.SubElement(notification_elem, "Published").text = published_time

# Convert to a string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)
