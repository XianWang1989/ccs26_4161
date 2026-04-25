
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Read text while handling special characters
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Print the text directly (No encoding/decoding needed)
print(docText.encode('utf-8'))
