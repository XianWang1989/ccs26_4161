
import xml.etree.ElementTree as ET

# Sample SOAP response data
notification_data = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the SOAP envelope
soap_env = ET.Element("soap:Envelope", {
    "xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

# Create the Body
soap_body = ET.SubElement(soap_env, "soap:Body")
response = ET.SubElement(soap_body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

# Result element
result = ET.SubElement(response, "GetNotificationsResult")

# Append NotificationData elements
for notification in notification_data:
    notification_element = ET.SubElement(result, "NotificationData")
    for key, value in notification.items():
        child = ET.SubElement(notification_element, key)
        child.text = str(value)

# Generate the final XML string
xml_string = ET.tostring(soap_env, encoding='unicode', method='xml')
print(xml_string)
