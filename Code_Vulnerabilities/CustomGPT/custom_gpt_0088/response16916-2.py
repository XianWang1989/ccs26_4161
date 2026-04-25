
def test_get_text():
    from xml.dom.minidom import parseString
    xml = "<root><Tag>525</Tag></root>"
    doc = parseString(xml)
    nodelist = doc.getElementsByTagName("Tag")
    print(getText(nodelist))

test_get_text()
