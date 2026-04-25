
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Read the text as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Now you can print the text without issues
print(docText)
