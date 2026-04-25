
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs without encoding to UTF-8 first
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print(docText)
