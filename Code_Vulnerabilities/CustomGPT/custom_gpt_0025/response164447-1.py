
import xml.etree.ElementTree as ET

# Sample SOAP response data
response_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the SOAP Envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the SOAP Body
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Create GetNotificationsResult
result = ET.SubElement(response, "GetNotificationsResult")

# Populate NotificationData elements
for notif in response_data:
    notification = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification, "Id").text = str(notif["Id"])
    ET.SubElement(notification, "Title").text = notif["Title"]
    ET.SubElement(notification, "Message").text = notif["Message"]
    ET.SubElement(notification, "Published").text = notif["Published"]

# Convert to string representation
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

print(xml_string)
