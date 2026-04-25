
import docx

# Load the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraph texts into a single string while keeping it as Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the docText as is, since it is already a Unicode object
print(docText.encode('utf-8'))  # encode to utf-8 for printing if needed
