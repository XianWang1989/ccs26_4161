
from xml.dom import minidom

# Example of using getText with a sample XML
xml_string = "<root><Tag>525</Tag></root>"
doc = minidom.parseString(xml_string)
nodelist = doc.getElementsByTagName('Tag')

text = getText(nodelist)
print(text)  # Output should be '525'
