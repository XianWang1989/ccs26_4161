import xml.etree.ElementTree as ET

xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<metalink version="3.0" xmlns="http://www.metalinker.org/" xmlns:lcgdm="LCGDM:" generator="lcgdm-dav" pubdate="Fri, 11 Oct 2013 12:46:10 GMT">
    <files>
        <file name="/lhcb/L">
            <size>173272912</size>
            <resources>
                <url type="https">https://test-kit.test.de:2880/pnfs/test.file</url>
                <url type="https">https://test.grid.sara.nl:2882/pnfs/test.file</url>
            </resources>
        </file>
    </files>
</metalink>'''

# Define the namespace dictionary
ns = {'ml': 'http://www.metalinker.org/'}

# Parse the XML
root = ET.fromstring(xml_string)

# Find all <url> elements using the namespace
urls = root.findall('.//ml:url', ns)

# Print the text content of each <url>
for url in urls:
    print(url.text)
