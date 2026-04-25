
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraph texts, ensuring they're treated as Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly since it's already a Unicode string
print(docText)
