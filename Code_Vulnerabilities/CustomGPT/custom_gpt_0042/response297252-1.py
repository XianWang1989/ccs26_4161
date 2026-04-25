
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraph texts, ensuring all are handled as Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly; no need to decode, as it's already Unicode
print(docText)
