
import docx

# Open the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Read the text and ensure it's stored as a Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly or encode it for output
print(docText.encode('utf-8'))
