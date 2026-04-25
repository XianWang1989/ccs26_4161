
import xml.etree.ElementTree as ET
import html

# Your XML string (escaped format)
xml_string = '''&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;metalink version="3.0" xmlns="http://www.metalinker.org/" xmlns:lcgdm="LCGDM:" generator="lcgdm-dav" pubdate="Fri, 11 Oct 2013 12:46:10 GMT"&gt;
&lt;files&gt;
&lt;file name="/lhcb/L"&gt;
&lt;size&gt;173272912&lt;/size&gt;
&lt;resources&gt;
&lt;url type="https"&gt;https://test-kit.test.de:2880/pnfs/test.file&lt;/url&gt;
&lt;url type="https"&gt;https://test.grid.sara.nl:2882/pnfs/test.file&lt;/url&gt;
&lt;/resources&gt;
&lt;/file&gt;
&lt;/files&gt;
&lt;/metalink&gt;'''

# Step 1: Unescape the HTML entities
unescaped_xml_string = html.unescape(xml_string)

# Step 2: Parse the XML
root = ET.fromstring(unescaped_xml_string)

# Step 3: Use XPath to extract <url> elements
namespaces = {'ns': 'http://www.metalinker.org/'}  # Define the namespace
urls = root.findall('.//ns:url', namespaces)

# Step 4: Print the URL text
for url in urls:
    print(url.text)
