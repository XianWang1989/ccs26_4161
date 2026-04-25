
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from paragraphs
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (Python 2.7 handles utf-8 automatically in print function)
print docText.encode('utf-8')  # Encode to UTF-8 for correct output
