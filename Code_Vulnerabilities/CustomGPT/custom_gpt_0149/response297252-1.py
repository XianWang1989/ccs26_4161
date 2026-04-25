
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs without encoding initially
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, as it will be Unicode
print(docText)
