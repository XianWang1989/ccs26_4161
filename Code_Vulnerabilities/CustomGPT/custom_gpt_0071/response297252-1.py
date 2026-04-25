
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs, ensuring it's in Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print or handle the text as needed
print(docText)
