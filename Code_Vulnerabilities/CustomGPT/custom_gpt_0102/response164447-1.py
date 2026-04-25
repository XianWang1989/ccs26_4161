
import xml.etree.ElementTree as ET
from datetime import datetime

# Example SOAP response data
response_data = {
    "NotificationData": [
        {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
        {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    ]
}

# Creating the SOAP envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Adding NotificationData
for notification in response_data["NotificationData"]:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_elem, "Published").text = published_date.strftime("%Y-%m-%dT%H:%M:%S")

# Generating the XML string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

# Output the formatted XML
print(xml_string)
