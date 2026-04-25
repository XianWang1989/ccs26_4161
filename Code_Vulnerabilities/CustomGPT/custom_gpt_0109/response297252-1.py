
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# To properly handle special characters, ensure proper encoding when printing
try:
    print(docText.encode('utf-8'))
except UnicodeEncodeError as e:
    print("Encoding error:", e)
