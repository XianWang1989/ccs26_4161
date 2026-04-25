
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs, handling special characters
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly without encoding error
print docText
