
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs  # Keep it as Unicode
])

# Print to console
print(docText.encode('utf-8'))  # Encode as UTF-8 for printing
