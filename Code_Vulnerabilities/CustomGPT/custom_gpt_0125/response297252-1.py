
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text without encoding it to bytes
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text directly (assuming UTF-8 handling in your environment)
print(docText)
