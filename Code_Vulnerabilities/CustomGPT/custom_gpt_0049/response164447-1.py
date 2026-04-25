
from suds.client import Client
from lxml import etree

# Sample SOAP response data, parsed into Python structures
soap_response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Creating the XML structure
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = etree.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

for notification in soap_response:
    notification_element = etree.SubElement(result, "{http://localhost/WS.asmx}NotificationData")
    for key, value in notification.items():
        item = etree.SubElement(notification_element, key)
        item.text = str(value)

# Converting the XML to a string
xml_str = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('UTF-8')

print(xml_str)
