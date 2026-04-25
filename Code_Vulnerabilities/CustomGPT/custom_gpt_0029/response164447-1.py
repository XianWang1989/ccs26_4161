
import xml.etree.ElementTree as ET

# Sample input as a list of dictionaries, simulating the SOAP response
notifications = [
    {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
    {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01 00:00:00"},
]

# Create the SOAP envelope
soap_ns = "http://schemas.xmlsoap.org/soap/envelope/"
response = ET.Element("{%s}Envelope" % soap_ns, {
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xsd": "http://www.w3.org/2001/XMLSchema"
})

body = ET.SubElement(response, "{%s}Body" % soap_ns)
notifications_response = ET.SubElement(body, "GetNotificationsResponse", {
    "xmlns": "http://localhost/WS.asmx"
})

result = ET.SubElement(notifications_response, "GetNotificationsResult")

# Add notification data to the XML structure
for notification in notifications:
    notification_data = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]
    ET.SubElement(notification_data, "Published").text = notification["Published"].replace(" ", "T")  # Format date

# Convert the XML tree to a string
xml_str = ET.tostring(response, encoding='unicode')

# Display the final XML
print(xml_str)
