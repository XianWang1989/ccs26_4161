
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Read the text from the document and encode it properly
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text to console
# Ensure to encode it properly for output
print(docText.encode('utf-8'))
