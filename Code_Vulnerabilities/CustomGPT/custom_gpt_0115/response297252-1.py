
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Construct the document text, ensuring proper handling of unicode characters
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the result directly without encoding
print docText
