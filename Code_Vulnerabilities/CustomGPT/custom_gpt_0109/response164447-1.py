
from lxml import etree

# Simulated SOAP response data
soap_response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the XML structure
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", nsmap={
    None: "http://schemas.xmlsoap.org/soap/envelope/",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xsd': "http://www.w3.org/2001/XMLSchema"
})

body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = etree.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Append NotificationData elements
for notification in soap_response:
    notification_data = etree.SubElement(result, "{http://localhost/WS.asmx}NotificationData")
    for key, value in notification.items():
        child = etree.SubElement(notification_data, key)
        child.text = str(value)

# Convert to string
xml_str = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode("utf-8")
print(xml_str)
