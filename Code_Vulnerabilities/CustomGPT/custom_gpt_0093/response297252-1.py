
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Construct the text using Unicode strings
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, no need to decode or encode
print(docText)
