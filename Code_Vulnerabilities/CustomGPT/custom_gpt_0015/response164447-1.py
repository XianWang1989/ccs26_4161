
from lxml import etree

# Sample SOAP response data
soap_response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root envelope
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", 
                         nsmap={None: "http://schemas.xmlsoap.org/soap/envelope/"})

body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")

# Add the result element
result = etree.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Convert each notification into XML
for notification in soap_response:
    notification_elem = etree.SubElement(result, "{http://localhost/WS.asmx}NotificationData")

    for key, value in notification.items():
        child = etree.SubElement(notification_elem, key)
        child.text = str(value)

# Convert to a string with pretty formatting
soap_xml = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode()

print(soap_xml)
