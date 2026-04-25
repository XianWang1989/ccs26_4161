
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Create an empty string for document text
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Print the document text which will now support special characters
print docText
