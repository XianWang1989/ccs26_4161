
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response
response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the root of the SOAP Envelope
soap_envelope = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

soap_body = ET.SubElement(soap_envelope, "soap:Body")
response_elem = ET.SubElement(soap_body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result_elem = ET.SubElement(response_elem, "GetNotificationsResult")

# Iterate over the notifications and construct XML
for notification in response:
    notification_elem = ET.SubElement(result_elem, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S").isoformat()
    ET.SubElement(notification_elem, "Published").text = published_date

# Convert to string and print
xml_string = ET.tostring(soap_envelope, encoding='unicode')
print(xml_string)
