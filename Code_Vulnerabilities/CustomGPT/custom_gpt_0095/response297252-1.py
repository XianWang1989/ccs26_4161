
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Use Unicode for text handling
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly; no need to decode
print(docText)
