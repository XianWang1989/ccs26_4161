
import xml.etree.ElementTree as ET

# Sample data based on the SOAP response given
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the main structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response = ET.SubElement(body, 'GetNotificationsResponse', {'xmlns': "http://localhost/WS.asmx"})
result = ET.SubElement(response, 'GetNotificationsResult')

# Populate NotificationData elements
for notification in notifications:
    notif_data = ET.SubElement(result, 'NotificationData')
    for key, value in notification.items():
        child = ET.SubElement(notif_data, key)
        child.text = value

# Convert to string
xml_str = ET.tostring(envelope, encoding='utf-8').decode('utf-8')
print(xml_str)
