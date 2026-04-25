
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Read paragraphs and handle encoding issues
docText = '\n\n'.join([
    paragraph.text.encode('utf-8', 'replace') for paragraph in document.paragraphs
])

# Decode the string to properly print with special characters
print(docText.decode('utf-8', 'replace'))
