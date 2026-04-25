
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs without encoding to utf-8
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text directly
print docText
