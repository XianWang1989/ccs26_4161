
from suds.client import Client
import xml.etree.ElementTree as ET

# Replace with your actual WSDL URL
wsdl_url = 'http://localhost/WS.asmx?WSDL'
client = Client(wsdl_url)

# Call your web service method and get the response
response = client.service.GetNotifications()

# Create the root of the SOAP envelope
envelope = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
body = ET.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

# Create the GetNotificationsResponse element
get_notifications_response = ET.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result = ET.SubElement(get_notifications_response, 'GetNotificationsResult')

# Assuming 'response' is a list of NotificationData objects
for notification in response:
    notification_elem = ET.SubElement(result, 'NotificationData')

    id_elem = ET.SubElement(notification_elem, 'Id')
    id_elem.text = str(notification.Id)

    title_elem = ET.SubElement(notification_elem, 'Title')
    title_elem.text = notification.Title

    message_elem = ET.SubElement(notification_elem, 'Message')
    message_elem.text = notification.Message

    published_elem = ET.SubElement(notification_elem, 'Published')
    published_elem.text = notification.Published.strftime('%Y-%m-%dT%H:%M:%S')  # Adjust format as needed

# Convert the XML structure to a string
xml_string = ET.tostring(envelope, encoding='unicode')

# Print the resulting XML
print(xml_string)
