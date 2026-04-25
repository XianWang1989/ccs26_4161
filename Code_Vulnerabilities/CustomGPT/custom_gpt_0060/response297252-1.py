
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs and join them
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Use print function with a safe output to handle Unicode characters
try:
    print(docText.encode('utf-8'))
except UnicodeEncodeError as e:
    print("Encoding error occurred:", e)
