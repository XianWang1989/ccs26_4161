
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs and handle encoding correctly
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text
print(docText.encode('utf-8'))
