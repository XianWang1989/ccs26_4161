
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect and encode the paragraphs in UTF-8
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, as it's already in Unicode
print(docText)
