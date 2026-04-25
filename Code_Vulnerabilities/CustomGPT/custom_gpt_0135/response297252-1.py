
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs and encode to utf-8
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Normally, you don't need to encode it explicitely if you are dealing with Unicode
try:
    print docText  # Directly print the text
except UnicodeEncodeError:
    # Handle the situation where encoding issues arise
    print docText.encode('utf-8')
