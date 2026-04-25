
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Create a Unicode string by joining the paragraph texts directly
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# If you need to encode it for output purposes, do it here
# For example, if you are writing to a file, encode it before writing
# Here we are just printing it (Unicode should work fine in most terminals)
print docText  # No need to decode, just print as it is

# If you are saving to a file, ensure to open the file correctly
# with the right encoding:
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(docText)
