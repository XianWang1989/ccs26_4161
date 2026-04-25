
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from the document, ensure it's Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode string directly
print(docText)
