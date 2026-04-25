
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text with proper handling of special characters
try:
    print docText.encode('utf-8')
except UnicodeEncodeError as e:
    print "Encoding Error: ", e
