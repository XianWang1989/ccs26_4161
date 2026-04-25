
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs as plain text (no encoding)
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print(docText)  # No need to decode
