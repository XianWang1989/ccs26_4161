
import xml.etree.ElementTree as ET
import re

# Mock SOAP response string
soap_response = "(ArrayOfNotificationData){NotificationData[] = (NotificationData){Id = 1 Title = \"notification 1\" Message = \"bla bla.\" Published = 2000-01-01 00:00:00}, (NotificationData){Id = 2 Title = \"notification 2\" Message = \"bla bla.\" Published = 2000-01-01 00:00:00},}"

# Extract NotificationData using regular expressions
pattern = r'\(NotificationData\){Id = (\d+) Title = "(.*?)" Message = "(.*?)" Published = (.*?)}'
notifications = re.findall(pattern, soap_response)

# Create the XML structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notifications:
    id_, title, message, published = notification
    notification_element = ET.SubElement(result, 'NotificationData')

    ET.SubElement(notification_element, 'Id').text = id_
    ET.SubElement(notification_element, 'Title').text = title
    ET.SubElement(notification_element, 'Message').text = message
    ET.SubElement(notification_element, 'Published').text = published.replace(" ", "T")

# Convert the XML structure to a string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)
