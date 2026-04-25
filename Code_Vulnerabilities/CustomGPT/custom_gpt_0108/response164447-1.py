
from suds.client import Client
from lxml import etree

# Create a SOAP client
client = Client('http://localhost/WS.asmx?WSDL')

# Call the web service method (assuming it's GetNotifications)
response = client.service.GetNotifications()

# Create the root of the SOAP envelope
soap_envelope = etree.Element(
    '{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
    nsmap={'soap': 'http://schemas.xmlsoap.org/soap/envelope/'}
)

soap_body = etree.SubElement(soap_envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')

# Create response structure
response_elem = etree.SubElement(soap_body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
result_elem = etree.SubElement(response_elem, 'GetNotificationsResult')

# Iterate through the response data and create XML elements
for notification in response.NotificationData:
    notification_elem = etree.SubElement(result_elem, 'NotificationData')

    id_elem = etree.SubElement(notification_elem, 'Id')
    id_elem.text = str(notification.Id)

    title_elem = etree.SubElement(notification_elem, 'Title')
    title_elem.text = notification.Title

    message_elem = etree.SubElement(notification_elem, 'Message')
    message_elem.text = notification.Message

    published_elem = etree.SubElement(notification_elem, 'Published')
    published_elem.text = notification.Published.isoformat()  # Adjust format as needed

# Convert the XML tree to a string
xml_string = etree.tostring(soap_envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('utf-8')

# Print or return the final XML
print(xml_string)
