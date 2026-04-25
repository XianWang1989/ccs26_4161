
from lxml import etree

# Sample input data
response = {
    "NotificationData": [
        {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
        {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
    ]
}

# Create the SOAP Envelope structure
envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response_elem = etree.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result_elem = etree.SubElement(response_elem, "{http://localhost/WS.asmx}GetNotificationsResult")

# Populate the NotificationData
for notification in response["NotificationData"]:
    notification_elem = etree.SubElement(result_elem, "NotificationData")
    etree.SubElement(notification_elem, "Id").text = str(notification["Id"])
    etree.SubElement(notification_elem, "Title").text = notification["Title"]
    etree.SubElement(notification_elem, "Message").text = notification["Message"]
    etree.SubElement(notification_elem, "Published").text = notification["Published"]

# Convert to string
soap_response_xml = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('utf-8')

# Print the result
print(soap_response_xml)
