
import xml.etree.ElementTree as ET

# The encoded XML string
xml_string = '''&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;metalink version="3.0" xmlns="http://www.metalinker.org/" xmlns:lcgdm="LCGDM:" generator="lcgdm-dav" pubdate="Fri, 11 Oct 2013 12:46:10 GMT"&gt;&lt;files&gt;&lt;file name="/lhcb/L"&gt;&lt;size&gt;173272912&lt;/size&gt;&lt;resources&gt;&lt;url type="https"&gt;https://test-kit.test.de:2880/pnfs/test.file&lt;/url&gt;&lt;url type="https"&gt;https://test.grid.sara.nl:2882/pnfs/test.file&lt;/url&gt;&lt;/resources&gt;&lt;/file&gt;&lt;/files&gt;&lt;/metalink&gt;'''

# Replace HTML entities back to XML format
xml_string = xml_string.replace('&lt;', '<').replace('&gt;', '>')

# Parse the XML string
root = ET.fromstring(xml_string)

# Use XPath to extract all <url> elements
urls = root.findall(".//{http://www.metalinker.org/}url")

# Print extracted URLs
for url in urls:
    print(url.text)
