
import xml.etree.ElementTree as ET

# Sample SOAP Response Data
notification_data = [
    {'Id': 1, 'Title': 'notification 1', 'Message': 'bla bla.', 'Published': '2000-01-01T00:00:00'},
    {'Id': 2, 'Title': 'notification 2', 'Message': 'bla bla.', 'Published': '2001-01-01T00:00:00'}
]

# Create the SOAP Envelope
soap_ns = "http://schemas.xmlsoap.org/soap/envelope/"
response_ns = "http://localhost/WS.asmx"

envelope = ET.Element(f"{{{soap_ns}}}Envelope")
body = ET.SubElement(envelope, f"{{{soap_ns}}}Body")
response = ET.SubElement(body, f"{{{response_ns}}}GetNotificationsResponse")
result = ET.SubElement(response, "GetNotificationsResult")

# Add NotificationData elements
for notification in notification_data:
    notification_element = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_element, "Id").text = str(notification['Id'])
    ET.SubElement(notification_element, "Title").text = notification['Title']
    ET.SubElement(notification_element, "Message").text = notification['Message']
    ET.SubElement(notification_element, "Published").text = notification['Published']

# Convert the XML to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')

print(xml_string)
