
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {
        "Id": 1,
        "Title": "notification 1",
        "Message": "bla bla.",
        "Published": "2000-01-01 00:00:00"
    },
    {
        "Id": 2,
        "Title": "notification 2",
        "Message": "bla bla.",
        "Published": "2001-01-01 00:00:00"
    }
]

# Create root elements for SOAP XML structure
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/", xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance", xmlns_xsd="http://www.w3.org/2001/XMLSchema")
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    ET.SubElement(notification_elem, "Published").text = notification["Published"].replace(" ", "T")  # Format date

# Convert to string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Print the final SOAP XML
print(xml_str)
