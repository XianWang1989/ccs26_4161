
import xml.etree.ElementTree as ET
from datetime import datetime

# Sample SOAP response data
notifications = [
    {'Id': 1, 'Title': "notification 1", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
    {'Id': 2, 'Title': "notification 2", 'Message': "bla bla.", 'Published': "2000-01-01 00:00:00"},
]

# Creating the root for the SOAP envelope
soap_env = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
soap_body = ET.SubElement(soap_env, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

# Creating the Response structure
response = ET.SubElement(soap_body, "GetNotificationsResponse", 
                         xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Adding notifications to the result
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification['Id'])
    ET.SubElement(notification_elem, "Title").text = notification['Title']
    ET.SubElement(notification_elem, "Message").text = notification['Message']

    # Format published date to ISO 8601
    published_date = datetime.strptime(notification['Published'], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(notification_elem, "Published").text = published_date.isoformat()

# Convert the tree to a string
xml_str = ET.tostring(soap_env, encoding='unicode')

# Print the final XML output
print(xml_str)
