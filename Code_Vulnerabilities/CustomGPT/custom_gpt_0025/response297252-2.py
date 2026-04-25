
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (Python 3 handles Unicode natively)
print(docText)
