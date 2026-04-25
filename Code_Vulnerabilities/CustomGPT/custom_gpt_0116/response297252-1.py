
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string, ensuring each paragraph is unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text, no decoding needed since it's already unicode
print docText
