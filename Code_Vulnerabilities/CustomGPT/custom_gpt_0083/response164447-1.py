
import xml.etree.ElementTree as ET

# Sample SOAP response structure
response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root SOAP Envelope
envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the SOAP Body
body = ET.SubElement(envelope, "soap:Body")

# Create the GetNotificationsResponse
response_element = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Create the GetNotificationsResult
result_element = ET.SubElement(response_element, "GetNotificationsResult")

# Populate NotificationData
for notification in response:
    notification_element = ET.SubElement(result_element, "NotificationData")

    ET.SubElement(notification_element, "Id").text = str(notification["Id"])
    ET.SubElement(notification_element, "Title").text = notification["Title"]
    ET.SubElement(notification_element, "Message").text = notification["Message"]
    ET.SubElement(notification_element, "Published").text = notification["Published"]

# Convert to a string and pretty print the XML
xml_str = ET.tostring(envelope, encoding='unicode')
print(xml_str)
