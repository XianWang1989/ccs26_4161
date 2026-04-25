
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text as Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print(docText)
