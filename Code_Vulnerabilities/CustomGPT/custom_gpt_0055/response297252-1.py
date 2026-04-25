
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs as Unicode strings
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# If you want to print this text (ensure it's in Unicode)
print(docText)
