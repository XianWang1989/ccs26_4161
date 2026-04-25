
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Use a Unicode string directly without encoding
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, as it should already be in Unicode
print(docText)
