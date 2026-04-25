
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Combine paragraphs into a single Unicode string
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Now, you can safely print the Unicode string
print(docText)
