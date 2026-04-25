
import docx

# Read the document and collect text
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, handling UTF-8
try:
    print docText.encode('utf-8')
except UnicodeEncodeError as e:
    print("Encoding error:", e)
