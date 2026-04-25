
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Concatenate paragraphs without encoding
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Now you can print it directly, or if necessary, encode when writing to a file
print docText
