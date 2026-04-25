
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraph texts without encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly as it’s already in Unicode
print(docText)
