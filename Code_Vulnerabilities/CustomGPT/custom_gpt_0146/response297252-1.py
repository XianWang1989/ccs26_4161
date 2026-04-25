
import docx

# Load the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string using Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text directly
print(docText)
