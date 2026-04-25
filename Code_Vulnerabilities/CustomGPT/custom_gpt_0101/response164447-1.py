
from suds.client import Client
from lxml import etree

# Assuming the SOAP client is already created
client = Client('http://localhost/WS.asmx?WSDL')
response = client.service.GetNotifications()

# Convert the response to XML
def convert_to_xml(response):
    envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    notifications_response = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
    result = etree.SubElement(notifications_response, "{http://localhost/WS.asmx}GetNotificationsResult")

    for notification in response:
        notification_data = etree.SubElement(result, "NotificationData")
        etree.SubElement(notification_data, "Id").text = str(notification.Id)
        etree.SubElement(notification_data, "Title").text = notification.Title
        etree.SubElement(notification_data, "Message").text = notification.Message
        etree.SubElement(notification_data, "Published").text = notification.Published.isoformat()

    return etree.tostring(envelope, pretty_print=True, encoding='unicode')

xml_output = convert_to_xml(response)
print(xml_output)
