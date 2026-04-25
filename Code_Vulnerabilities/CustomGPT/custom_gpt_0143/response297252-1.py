
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs and handle encoding properly
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly without encoding to avoid errors
print(docText)
