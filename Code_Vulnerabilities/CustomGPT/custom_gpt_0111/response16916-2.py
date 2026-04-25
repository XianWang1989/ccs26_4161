
from xml.dom.minidom import Document

# Mocking a nodelist for demonstration
doc = Document()
tag = doc.createElement("Tag")
text_node = doc.createTextNode("525")
tag.appendChild(text_node)

nodelist = [tag.firstChild]  # Simulating a nodelist containing the text node

result = getText(nodelist)
print(result)  # Output should be '525'
