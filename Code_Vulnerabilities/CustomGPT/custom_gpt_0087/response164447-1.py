
import xml.etree.ElementTree as ET

# Sample notifications
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root elements
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

result = ET.SubElement(response, "GetNotificationsResult")

# Adding NotificationData elements
for notification in notifications:
    notification_element = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_element, "Id").text = str(notification["Id"])
    ET.SubElement(notification_element, "Title").text = notification["Title"]
    ET.SubElement(notification_element, "Message").text = notification["Message"]
    ET.SubElement(notification_element, "Published").text = notification["Published"]

# Generate the XML string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)
