
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join all paragraphs into a single string
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print docText
