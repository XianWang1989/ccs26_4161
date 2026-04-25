
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root of the SOAP XML
envelope = Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = SubElement(response, "GetNotificationsResult")

# Iterate over notifications and build XML
for notification in notifications:
    notification_data = SubElement(result, "NotificationData")
    SubElement(notification_data, "Id").text = str(notification["Id"])
    SubElement(notification_data, "Title").text = notification["Title"]
    SubElement(notification_data, "Message").text = notification["Message"]
    SubElement(notification_data, "Published").text = notification["Published"]

# Convert the XML to a string
xml_string = tostring(envelope, encoding='unicode')

# Print or save the XML
print(xml_string)
