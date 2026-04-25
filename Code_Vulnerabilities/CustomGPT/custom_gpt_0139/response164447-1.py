
from suds.client import Client
from lxml import etree

# URL of the SOAP web service
wsdl_url = 'http://localhost/WS.asmx?WSDL'

# Create a suds client
client = Client(wsdl_url)

# Call the method to get notifications
response = client.service.GetNotifications()

# Assuming the response is a list of notification data structures
# We can process it to build XML
def convert_to_xml(notification_data):
    # Create the main XML structure
    namespaces = {'soap': 'http://schemas.xmlsoap.org/soap/envelope/'}
    envelope = etree.Element('{%s}Envelope' % namespaces['soap'], nsmap=namespaces)
    body = etree.SubElement(envelope, '{%s}Body' % namespaces['soap'])
    response_element = etree.SubElement(body, 'GetNotificationsResponse', xmlns="http://localhost/WS.asmx")
    result_element = etree.SubElement(response_element, 'GetNotificationsResult')

    # Loop through notifications to create XML elements
    for notification in notification_data:
        notification_element = etree.SubElement(result_element, 'NotificationData')
        etree.SubElement(notification_element, 'Id').text = str(notification.Id)
        etree.SubElement(notification_element, 'Title').text = notification.Title
        etree.SubElement(notification_element, 'Message').text = notification.Message
        etree.SubElement(notification_element, 'Published').text = notification.Published.strftime("%Y-%m-%dT%H:%M:%S")

    return etree.tostring(envelope, pretty_print=True).decode()

# Convert response to XML format
xml_output = convert_to_xml(response)
print(xml_output)
