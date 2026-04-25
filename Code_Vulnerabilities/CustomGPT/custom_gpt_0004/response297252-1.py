
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs as Unicode text
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode text (encoding for console output)
print docText.encode('utf-8')
