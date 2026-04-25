
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs and handle encoding
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Print the text without decoding issues
print(docText.encode('utf-8'))
