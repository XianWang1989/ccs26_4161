
import xml.etree.ElementTree as ET

def convert_soap_response_to_xml(response):
    root = ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body = ET.SubElement(root, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    response_elem = ET.SubElement(body, "GetNotificationsResponse", 
                                   xmlns="http://localhost/WS.asmx")
    result_elem = ET.SubElement(response_elem, "GetNotificationsResult")

    notifications = [
        {"Id": 1, "Title": "notification 1", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"},
        {"Id": 2, "Title": "notification 2", "Message": "bla bla.", "Published": "2000-01-01T00:00:00"}
    ]

    for notification in notifications:
        notification_elem = ET.SubElement(result_elem, "NotificationData")
        ET.SubElement(notification_elem, "Id").text = str(notification["Id"])
        ET.SubElement(notification_elem, "Title").text = notification["Title"]
        ET.SubElement(notification_elem, "Message").text = notification["Message"]
        ET.SubElement(notification_elem, "Published").text = notification["Published"]

    xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True).decode()
    print(xml_str)

convert_soap_response_to_xml(None)
