
from suds.client import Client
from lxml import etree
from datetime import datetime

# Example SOAP client initialization
url = "http://localhost/WS.asmx?wsdl"
client = Client(url)

# Fetching notifications
response = client.service.GetNotifications()

# Sample response structure
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create SOAP XML structure
soap_env = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
soap_body = etree.SubElement(soap_env, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response_elem = etree.SubElement(soap_body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result_elem = etree.SubElement(response_elem, "GetNotificationsResult")

# Adding notifications to the XML
for notification in notifications:
    notification_elem = etree.SubElement(result_elem, "NotificationData")
    etree.SubElement(notification_elem, "Id").text = str(notification["Id"])
    etree.SubElement(notification_elem, "Title").text = notification["Title"]
    etree.SubElement(notification_elem, "Message").text = notification["Message"]
    published_date = datetime.strptime(notification["Published"], "%Y-%m-%d %H:%M:%S").isoformat()
    etree.SubElement(notification_elem, "Published").text = published_date

# Convert to string
soap_xml = etree.tostring(soap_env, pretty_print=True, encoding='unicode')

print(soap_xml)
