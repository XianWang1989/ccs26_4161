
import xml.etree.ElementTree as ET

# Sample response from SOAP service
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root element
soap_env = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/")
soap_body = ET.SubElement(soap_env, "soap:Body")

# Create the GetNotificationsResponse element
response = ET.SubElement(soap_body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Loop through the notifications to create NotificationData elements
for data in notification_data:
    notification = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification, "Id").text = str(data["Id"])
    ET.SubElement(notification, "Title").text = data["Title"]
    ET.SubElement(notification, "Message").text = data["Message"]
    # Convert the published date to proper format (ISO 8601)
    published_date = data["Published"].replace(" ", "T")
    ET.SubElement(notification, "Published").text = published_date

# Convert the constructed XML tree to a string
xml_string = ET.tostring(soap_env, encoding='utf-8', xml_declaration=True)

# Pretty-print the XML
import xml.dom.minidom

xml_pretty = xml.dom.minidom.parseString(xml_string).toprettyxml(indent="    ")
print(xml_pretty)
