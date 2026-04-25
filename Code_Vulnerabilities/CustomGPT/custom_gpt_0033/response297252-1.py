
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Gather the text without encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print docText
