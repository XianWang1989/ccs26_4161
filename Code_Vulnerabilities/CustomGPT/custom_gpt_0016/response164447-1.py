
from suds.client import Client
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Assuming you have your SOAP client set up
soap_url = 'http://localhost/WS.asmx?WSDL'
client = Client(soap_url)

# Call the web service (modify with the proper method and parameters)
response = client.service.GetNotifications()

# Function to convert your notification data to XML
def create_soap_response(notifications):
    envelope = Element('soap:Envelope', {
        'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
    })

    body = SubElement(envelope, 'soap:Body')
    response_element = SubElement(body, 'GetNotificationsResponse', {'xmlns': "http://localhost/WS.asmx"})
    result_element = SubElement(response_element, 'GetNotificationsResult')

    for notification in notifications:
        notification_element = SubElement(result_element, 'NotificationData')
        SubElement(notification_element, 'Id').text = str(notification['Id'])
        SubElement(notification_element, 'Title').text = notification['Title']
        SubElement(notification_element, 'Message').text = notification['Message']
        SubElement(notification_element, 'Published').text = notification['Published'].isoformat()

    return tostring(envelope, 'utf-8')

# Example conversion (would depend on the structure of response)
# Assuming response is structured similarly to the NotificationData above
# e.g. response = [{"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": datetime_object}, ...]

xml_output = create_soap_response(response)
pretty_xml = minidom.parseString(xml_output).toprettyxml()

print(pretty_xml)
