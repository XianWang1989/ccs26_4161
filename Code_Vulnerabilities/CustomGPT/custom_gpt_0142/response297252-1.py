
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Create a string that contains the document's text
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Encoding the output for the console
try:
    print docText  # Print without encoding to automatically use the console's default encoding
except UnicodeEncodeError:
    # If there's a UnicodeEncodeError, try encoding to 'utf-8' explicitly
    print docText.encode('utf-8')
