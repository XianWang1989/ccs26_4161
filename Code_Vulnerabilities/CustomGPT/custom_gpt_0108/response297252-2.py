
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Read and join paragraphs as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text
print(docText)
