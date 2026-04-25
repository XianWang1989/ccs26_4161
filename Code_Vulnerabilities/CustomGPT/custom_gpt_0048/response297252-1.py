
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs while staying in unicode
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the unicode string directly
print docText
