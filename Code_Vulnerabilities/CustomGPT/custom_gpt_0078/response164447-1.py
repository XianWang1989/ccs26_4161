
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the root of the SOAP envelope
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

# Create the body element
body = ET.SubElement(envelope, 'soap:Body')

# Create the response element
response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, 'GetNotificationsResult')

# Append NotificationData elements
for notification in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_data, 'Title').text = notification['Title']
    ET.SubElement(notification_data, 'Message').text = notification['Message']
    ET.SubElement(notification_data, 'Published').text = notification['Published']

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the XML
print(xml_str)
