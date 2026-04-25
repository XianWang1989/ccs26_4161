
import xml.etree.ElementTree as ET

# Simulated SOAP response data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the main envelope element
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the Body element
body = ET.SubElement(envelope, "soap:Body")

# Create response element
response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Create the GetNotificationsResult element
result = ET.SubElement(response, "GetNotificationsResult")

# Iterate over notification data and create subelements
for notification in notification_data:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    ET.SubElement(notification_elem, "Published").text = notification["Published"]

# Convert to string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print final XML
print(xml_string)
