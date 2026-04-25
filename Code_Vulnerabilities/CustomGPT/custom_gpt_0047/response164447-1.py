
import xml.etree.ElementTree as ET

# Sample response data (simulating the parsed SOAP response)
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root element
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                      xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                      xmlns_xsd="http://www.w3.org/2001/XMLSchema")
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", 
                          xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Populate the NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]
    ET.SubElement(notification_data, "Published").text = notification["Published"]

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode')
print(xml_str)
