
import xml.etree.ElementTree as ET

# Sample SOAP response data
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the main elements
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')
result = ET.SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

# Add NotificationData to the result
for notification in notifications:
    notification_data = ET.SubElement(result, '{http://localhost/WS.asmx}NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notification['Id'])
    ET.SubElement(notification_data, 'Title').text = notification['Title']
    ET.SubElement(notification_data, 'Message').text = notification['Message']
    ET.SubElement(notification_data, 'Published').text = notification['Published']

# Generate the XML string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print the XML
print(xml_string)
