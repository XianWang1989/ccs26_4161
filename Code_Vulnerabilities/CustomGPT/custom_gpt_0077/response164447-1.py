
import xml.etree.ElementTree as ET

# Sample SOAP response data
response_data = {
    "NotificationData": [
        {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
        {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
    ]
}

# Create the SOAP envelope structure
soap_ns = "http://schemas.xmlsoap.org/soap/envelope/"
response_ns = "http://localhost/WS.asmx"

envelope = ET.Element("{%s}Envelope" % soap_ns, xmlns_soap=soap_ns)
body = ET.SubElement(envelope, "{%s}Body" % soap_ns)
get_notifications_response = ET.SubElement(body, "{%s}GetNotificationsResponse" % response_ns)
get_notifications_result = ET.SubElement(get_notifications_response, "{%s}GetNotificationsResult" % response_ns)

# Add NotificationData elements
for notification in response_data["NotificationData"]:
    notification_data = ET.SubElement(get_notifications_result, "{%s}NotificationData" % response_ns)
    ET.SubElement(notification_data, "Id").text = str(notification["Id"])
    ET.SubElement(notification_data, "Title").text = notification["Title"]
    ET.SubElement(notification_data, "Message").text = notification["Message"]
    ET.SubElement(notification_data, "Published").text = notification["Published"]

# Convert the tree to a string
xml_string = ET.tostring(envelope, encoding='unicode')
print(xml_string)

# Optionally, if you need to save to a file
# with open("response.xml", "w") as f:
#     f.write(xml_string)
