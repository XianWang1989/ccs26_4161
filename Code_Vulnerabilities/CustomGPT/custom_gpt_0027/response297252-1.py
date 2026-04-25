
import docx
import codecs

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Create a UTF-8 encoded string from the document paragraphs
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Encode to utf-8 and decode with error handling
encoded_text = codecs.encode(docText, 'utf-8', errors='replace')

# Print the text
print(encoded_text)
