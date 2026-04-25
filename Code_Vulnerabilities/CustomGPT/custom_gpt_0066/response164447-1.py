
from suds.client import Client
from lxml import etree

# Assuming you have the URL of your WSDL
service_url = 'http://localhost/WS.asmx?WSDL'
client = Client(service_url)

# Call the web service method (replace GetNotifications with your actual method)
response = client.service.GetNotifications()

# Parse the SOAP response (example format)
notifications = response.NotificationData

# Construct the SOAP XML response
soap_ns = 'http://schemas.xmlsoap.org/soap/envelope/'
body = etree.Element('{%s}Body' % soap_ns)

# Create the GetNotificationsResponse element
response_element = etree.SubElement(body, 'GetNotificationsResponse', 
                                     xmlns="http://localhost/WS.asmx")
result_element = etree.SubElement(response_element, 'GetNotificationsResult')

# Add NotificationData elements
for notification in notifications:
    notification_element = etree.SubElement(result_element, 'NotificationData')
    id_element = etree.SubElement(notification_element, 'Id')
    id_element.text = str(notification.Id)
    title_element = etree.SubElement(notification_element, 'Title')
    title_element.text = notification.Title
    message_element = etree.SubElement(notification_element, 'Message')
    message_element.text = notification.Message
    published_element = etree.SubElement(notification_element, 'Published')
    published_element.text = notification.Published.strftime('%Y-%m-%dT%H:%M:%S')

# Generate the final XML string
xml_string = etree.tostring(body, pretty_print=True).decode('utf-8')
print(xml_string)
