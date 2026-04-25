
import xml.etree.ElementTree as ET
from suds.client import Client

# Assuming you have the endpoint for your SOAP web service
wsdl_url = 'http://localhost/WS.asmx?WSDL'
client = Client(wsdl_url)

# Call the SOAP method
response = client.service.GetNotifications()

# Example response handling. 
# Let's say response is a list of NotificationData objects as expected.

# Create the root element for the SOAP Envelope
envelope = ET.Element('soap:Envelope', 
                       xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
                       xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                       xmlns_xsd="http://www.w3.org/2001/XMLSchema")

# Create the Body element
body = ET.SubElement(envelope, 'soap:Body')

# Create the GetNotificationsResponse element
get_notifications_response = ET.SubElement(body, 'GetNotificationsResponse', 
                                            xmlns="http://localhost/WS.asmx")

# Create the GetNotificationsResult element
get_notifications_result = ET.SubElement(get_notifications_response, 'GetNotificationsResult')

# Iterate through each notification in the response
for notification in response:
    notification_data = ET.SubElement(get_notifications_result, 'NotificationData')

    # Creating the Id element
    id_element = ET.SubElement(notification_data, 'Id')
    id_element.text = str(notification.Id)

    # Creating the Title element
    title_element = ET.SubElement(notification_data, 'Title')
    title_element.text = notification.Title

    # Creating the Message element
    message_element = ET.SubElement(notification_data, 'Message')
    message_element.text = notification.Message

    # Creating the Published element
    published_element = ET.SubElement(notification_data, 'Published')
    published_element.text = notification.Published.strftime('%Y-%m-%dT%H:%M:%S')  # Adjust format as needed

# Convert the ElementTree to a string
xml_response = ET.tostring(envelope, encoding='utf-8', method='xml').decode('utf-8')

# Print or return the XML response
print(xml_response)
