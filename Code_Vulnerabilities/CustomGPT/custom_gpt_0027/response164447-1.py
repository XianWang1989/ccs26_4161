
from suds.client import Client
from suds.sax.element import Element
import datetime

# Example SOAP response data
soap_response = {
    'NotificationData': [
        {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
        {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
    ]
}

# Create a function to build the desired XML structure
def build_soap_response(data):
    envelope = Element('Envelope', {
        'xmlns:soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
    })
    body = Element('Body')
    response = Element('GetNotificationsResponse', {
        'xmlns': "http://localhost/WS.asmx"
    })
    result = Element('GetNotificationsResult')

    for item in data['NotificationData']:
        notification = Element('NotificationData')
        notification.append(Element('Id', str(item['Id'])))
        notification.append(Element('Title', item['Title']))
        notification.append(Element('Message', item['Message']))

        # Convert published date to the required format
        published_date = datetime.datetime.strptime(item['Published'], "%Y-%m-%d %H:%M:%S").isoformat()
        notification.append(Element('Published', published_date))

        result.append(notification)

    response.append(result)
    body.append(response)
    envelope.append(body)

    return envelope

# Create the XML structure
soap_xml = build_soap_response(soap_response)

# Print the resulting SOAP XML
print(soap_xml)
