
import xml.etree.ElementTree as ET

# Sample response data as a list of dictionaries
notifications = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"}
]

# Create the root element for the SOAP Envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

# Create GetNotificationsResponse element
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Loop through the notifications and create XML elements
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification['Id'])
    ET.SubElement(notification_data, "Title").text = notification['Title']
    ET.SubElement(notification_data, "Message").text = notification['Message']
    ET.SubElement(notification_data, "Published").text = notification['Published']

# Generate the XML string
xml_string = ET.tostring(envelope, encoding='unicode')

print(xml_string)
