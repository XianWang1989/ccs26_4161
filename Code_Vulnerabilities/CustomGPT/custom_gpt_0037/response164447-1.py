
import xml.etree.ElementTree as ET

# Sample SOAP response as a dictionary mimicking the structure
soap_response = {
    "NotificationData": [
        {
            "Id": 1,
            "Title": "notification 1",
            "Message": "bla bla.",
            "Published": "2000-01-01T00:00:00"
        },
        {
            "Id": 2,
            "Title": "notification 2",
            "Message": "bla bla.",
            "Published": "2000-01-01T00:00:00"
        }
    ]
}

# Create the XML structure
envelope = ET.Element("soap:Envelope", xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/")
body = ET.SubElement(envelope, "soap:Body")
response = ET.SubElement(body, "GetNotificationsResponse", xmlns="http://localhost/WS.asmx")
result = ET.SubElement(response, "GetNotificationsResult")

# Add each NotificationData element
for notification in soap_response["NotificationData"]:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    ET.SubElement(notification_elem, "Published").text = notification["Published"]

# Convert to a string
xml_string = ET.tostring(envelope, encoding='unicode', method='xml')
print(xml_string)
