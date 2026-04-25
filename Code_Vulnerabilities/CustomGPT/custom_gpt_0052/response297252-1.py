
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Print the string (it should already be in Unicode)
print(docText)
