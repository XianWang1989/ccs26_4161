
from suds.client import Client
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from datetime import datetime

# Example SOAP client setup
client = Client('http://localhost/WS.asmx?WSDL')

# Call the web service method
response = client.service.GetNotifications()

# Example structure to hold the XML
soap_env = Element('soap:Envelope', {
    'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
})

soap_body = SubElement(soap_env, 'soap:Body')
get_notifications_response = SubElement(soap_body, 'GetNotificationsResponse', {
    'xmlns': "http://localhost/WS.asmx"
})
get_notifications_result = SubElement(get_notifications_response, 'GetNotificationsResult')

# Parse response and construct XML structure
for notification in response:
    notification_data = SubElement(get_notifications_result, 'NotificationData')
    SubElement(notification_data, 'Id').text = str(notification.Id)
    SubElement(notification_data, 'Title').text = notification.Title
    SubElement(notification_data, 'Message').text = notification.Message
    published_time = datetime.strptime(notification.Published, '%Y-%m-%d %H:%M:%S')
    SubElement(notification_data, 'Published').text = published_time.isoformat()

# Convert XML to string
xml_string = tostring(soap_env, encoding='unicode')
print(xml_string)
