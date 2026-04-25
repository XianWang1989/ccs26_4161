
from suds.client import Client
from lxml import etree

# Replace with your actual WSDL URL
wsdl_url = 'http://localhost/WS.asmx?WSDL'
client = Client(wsdl_url)

# Assuming 'GetNotifications' is the method you invoke
response = client.service.GetNotifications()

# Parse the response (this will depend on actual response structure)
notifications = response.NotificationData

# Creating the SOAP XML structure
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope",
                          nsmap={None: "http://schemas.xmlsoap.org/soap/envelope/"})
body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response_elem = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result_elem = etree.SubElement(response_elem, "{http://localhost/WS.asmx}GetNotificationsResult")

for notification in notifications:
    notification_elem = etree.SubElement(result_elem, "{http://localhost/WS.asmx}NotificationData")
    etree.SubElement(notification_elem, "Id").text = str(notification.Id)
    etree.SubElement(notification_elem, "Title").text = notification.Title
    etree.SubElement(notification_elem, "Message").text = notification.Message
    etree.SubElement(notification_elem, "Published").text = notification.Published.isoformat()

# Generate the XML string
xml_string = etree.tostring(envelope, pretty_print=True).decode()

print(xml_string)
