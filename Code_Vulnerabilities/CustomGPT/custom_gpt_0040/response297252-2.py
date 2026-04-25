
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs and join them with double newlines
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Properly handle printing with encoding
try:
    print(docText.encode('utf-8'))
except UnicodeEncodeError:
    print("Encoding error occurred.")
