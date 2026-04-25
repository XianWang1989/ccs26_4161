
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs as Unicode strings
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text, as it is already in Unicode
print docText
