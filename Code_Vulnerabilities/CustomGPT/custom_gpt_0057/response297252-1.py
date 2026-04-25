
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect the paragraphs as a UTF-8 encoded string
doc_text = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the string directly, as it's already unicode
print(doc_text)
