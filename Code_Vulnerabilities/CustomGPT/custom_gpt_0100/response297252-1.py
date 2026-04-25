
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')
# Join the paragraphs, keeping them as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly without encoding
print(docText)
