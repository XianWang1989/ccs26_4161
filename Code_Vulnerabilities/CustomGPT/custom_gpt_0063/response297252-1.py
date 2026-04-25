
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# To safely print, handle encoding with a try-except block
try:
    print(docText.encode('utf-8'))  # Encode to UTF-8 for printing
except UnicodeEncodeError:
    # Handle potential encoding issues
    print("Encoding error occurred. Some characters may not display correctly.")
