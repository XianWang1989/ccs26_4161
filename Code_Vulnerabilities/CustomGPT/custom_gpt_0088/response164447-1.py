
import xml.etree.ElementTree as ET

# Example data simulating the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
]

# Create the root elements for the SOAP response
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")

response = ET.SubElement(body, "GetNotificationsResponse", {"xmlns": "http://localhost/WS.asmx"})
result = ET.SubElement(response, "GetNotificationsResult")

# Adding NotificationData elements
for notif in notifications:
    notification = ET.SubElement(result, "NotificationData")
    for key, value in notif.items():
        ET.SubElement(notification, key).text = str(value)

# Convert the ElementTree to a string
soap_response = ET.tostring(envelope, encoding='unicode')

# Print the SOAP response XML
print(soap_response)
