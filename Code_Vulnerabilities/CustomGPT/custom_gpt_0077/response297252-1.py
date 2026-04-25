
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (Python 2.7 handles Unicode)
print docText
