
import docx

# Open the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Use a list to collect the text
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly since it's already in Unicode
print docText
