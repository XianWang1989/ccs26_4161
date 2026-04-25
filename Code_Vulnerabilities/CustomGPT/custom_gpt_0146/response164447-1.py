
from lxml import etree

# Assume we have the following list of notifications received from the SOAP response
notification_data = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01T00:00:00"}
]

# Create a root element for the SOAP Envelope
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", nsmap={
    'soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xsd': "http://www.w3.org/2001/XMLSchema"
})

# Create Body element
body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = etree.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = etree.SubElement(response, "GetNotificationsResult")

# Loop through each notification and append to the result
for notification in notification_data:
    notification_elem = etree.SubElement(result, "NotificationData")
    etree.SubElement(notification_elem, "Id").text = str(notification['Id'])
    etree.SubElement(notification_elem, "Title").text = notification['Title']
    etree.SubElement(notification_elem, "Message").text = notification['Message']
    etree.SubElement(notification_elem, "Published").text = notification['Published']

# Generate the XML string
xml_str = etree.tostring(envelope, encoding='unicode', pretty_print=True)

# Print the resulting XML
print(xml_str)
