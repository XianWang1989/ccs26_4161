
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Build the text from paragraphs as Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text, ensuring we handle encoding properly
print(docText.encode('utf-8'))
