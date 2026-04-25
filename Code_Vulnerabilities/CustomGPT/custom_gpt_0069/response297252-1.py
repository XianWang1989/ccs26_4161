
import docx

# Open the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Use unicode to handle paragraphs directly
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the result directly, no need to decode since it's already a unicode string
print(docText)
