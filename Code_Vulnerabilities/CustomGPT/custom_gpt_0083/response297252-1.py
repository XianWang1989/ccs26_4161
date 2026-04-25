
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Ensure text is collected as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (it's already in Unicode)
print docText
