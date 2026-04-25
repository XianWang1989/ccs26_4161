
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect the paragraphs directly as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the content, handling special characters
print(docText.encode('utf-8'))
