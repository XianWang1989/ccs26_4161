
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs directly
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print without encoding
print docText
