
import xml.etree.ElementTree as ET

# Sample response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the SOAP Envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", 
                       xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                       xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                       xmlns_xsd="http://www.w3.org/2001/XMLSchema")

body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Add each notification to the XML
for notification in notifications:
    notif_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notif_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notif_elem, "Title").text = notification["Title"]
    ET.SubElement(notif_elem, "Message").text = notification["Message"]
    ET.SubElement(notif_elem, "Published").text = notification["Published"]

# Convert to string
xml_str = ET.tostring(envelope, encoding='unicode', method='xml')

# Display the result
print(xml_str)
