
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the XML structure
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/")
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Populate NotificationData elements
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    ET.SubElement(notification_elem, "Published").text = notification["Published"].replace(" ", "T")

# Convert to a string
xml_string = ET.tostring(envelope, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Pretty print the XML for better readability
import xml.dom.minidom
xml_pretty = xml.dom.minidom.parseString(xml_string).toprettyxml()

# Output the pretty printed XML
print(xml_pretty)
