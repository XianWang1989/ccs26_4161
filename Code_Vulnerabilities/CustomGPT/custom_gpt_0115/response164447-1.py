
import xml.etree.ElementTree as ET

# Sample data as provided in the response
notifications = [
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

# Create the root envelope
envelope = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
body = ET.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
response = ET.SubElement(body, "{http://localhost/WS.asmx}GetNotificationsResponse")
result = ET.SubElement(response, "{http://localhost/WS.asmx}GetNotificationsResult")

# Append notifications to the result
for notification in notifications:
    notification_elem = ET.SubElement(result, "NotificationData")
    ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
    ET.SubElement(notification_elem, "Title").text = notification["Title"]
    ET.SubElement(notification_elem, "Message").text = notification["Message"]
    ET.SubElement(notification_elem, "Published").text = notification["Published"]

# Convert to a string
xml_string = ET.tostring(envelope, encoding='utf-8').decode('utf-8')
print(xml_string)
