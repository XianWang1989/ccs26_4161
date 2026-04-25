
import xml.etree.ElementTree as ET

# Simulated input from the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
]

# Create the root SOAP envelope
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
response = ET.SubElement(body, '{http://localhost/WS.asmx}GetNotificationsResponse')

# Create the GetNotificationsResult element
result = ET.SubElement(response, '{http://localhost/WS.asmx}GetNotificationsResult')

# Iterate over notifications and add them to XML
for notif in notifications:
    notification_data = ET.SubElement(result, 'NotificationData')
    ET.SubElement(notification_data, 'Id').text = str(notif["Id"])
    ET.SubElement(notification_data, 'Title').text = notif["Title"]
    ET.SubElement(notification_data, 'Message').text = notif["Message"]
    ET.SubElement(notification_data, 'Published').text = notif["Published"]

# Convert the ElementTree to a string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print the resulting XML
print(xml_string)
