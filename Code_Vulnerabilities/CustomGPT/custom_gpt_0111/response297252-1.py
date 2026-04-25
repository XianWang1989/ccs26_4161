
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs text
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text directly
# Ensure the console can handle UTF-8
try:
    print docText.encode('utf-8')
except UnicodeEncodeError:
    print "Encoding error occurred"
