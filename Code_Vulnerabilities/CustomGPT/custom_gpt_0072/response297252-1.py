
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Gather all paragraphs and join them into a single string
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, Python 2.7 handles it without explicit encode/decode
print(docText)
