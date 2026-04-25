
import xml.etree.ElementTree as ET

# Your XML string (escaped with HTML entities)
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

# Parse the XML string
root = ET.fromstring(xml_string)

# Use XPath to extract all URLs
namespaces = {'m': 'http://www.metalinker.org/'}
urls = root.findall('.//m:url', namespaces)

# Print extracted URLs
for url in urls:
    print(url.text)
