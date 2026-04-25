
import xml.etree.ElementTree as ET

# Sample soap response
response_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create SOAP Envelope
soap_env = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/")
soap_body = ET.SubElement(soap_env, "soap:Body")
response = ET.SubElement(soap_body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for notification in response_data:
    notification_elem = ET.SubElement(result, "NotificationData")

    id_elem = ET.SubElement(notification_elem, "Id")
    id_elem.text = str(notification["Id"])

    title_elem = ET.SubElement(notification_elem, "Title")
    title_elem.text = notification["Title"]

    message_elem = ET.SubElement(notification_elem, "Message")
    message_elem.text = notification["Message"]

    published_elem = ET.SubElement(notification_elem, "Published")
    published_elem.text = notification["Published"]

# Generate XML string
xml_str = ET.tostring(soap_env, encoding="unicode")
print(xml_str)
