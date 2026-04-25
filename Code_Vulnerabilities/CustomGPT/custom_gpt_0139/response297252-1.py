
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Use unicode strings and join paragraphs
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode string directly
print docText
