
from suds.client import Client
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Create a SOAP client
url = 'http://localhost/WS.asmx?WSDL'
client = Client(url)

# Call the web service method to get notifications
response = client.service.GetNotifications()  # Adjust the method name as necessary

# Parse the response into desired XML structure
def create_soap_xml(notifications):
    envelope = Element('soap:Envelope', {
        'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
    })

    body = SubElement(envelope, 'soap:Body')
    get_notifications_response = SubElement(body, 'GetNotificationsResponse', {
        'xmlns': "http://localhost/WS.asmx"
    })

    get_notifications_result = SubElement(get_notifications_response, 'GetNotificationsResult')

    for notification in notifications:
        notification_data = SubElement(get_notifications_result, 'NotificationData')

        SubElement(notification_data, 'Id').text = str(notification.Id)
        SubElement(notification_data, 'Title').text = notification.Title
        SubElement(notification_data, 'Message').text = notification.Message
        SubElement(notification_data, 'Published').text = notification.Published.isoformat()  # Format to ISO 8601

    return tostring(envelope, encoding='unicode')

# Assuming `response` has a 'NotificationData' attribute
xml_output = create_soap_xml(response.NotificationData)
print(xml_output)
