
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response
response = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"}
]

# Create the main SOAP structure
envelope = ET.Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(envelope, 'soap:Body')
response_element = ET.SubElement(body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
result_element = ET.SubElement(response_element, 'GetNotificationsResult')

# Add NotificationData
for notification in response:
    notification_element = ET.SubElement(result_element, 'NotificationData')

    for key, value in notification.items():
        if key == "Published":
            value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S').isoformat()
        ET.SubElement(notification_element, key).text = str(value)

# Generate the XML string
xml_str = ET.tostring(envelope, encoding='unicode')

# Print the XML
print(xml_str)
