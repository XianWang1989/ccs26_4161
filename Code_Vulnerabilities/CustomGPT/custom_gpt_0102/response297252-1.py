
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs as Unicode
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text, encoding it to UTF-8 while handling errors
print(docText.encode('utf-8', errors='replace'))
