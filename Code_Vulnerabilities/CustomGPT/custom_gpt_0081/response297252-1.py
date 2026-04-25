
import docx
import sys

# Set the default encoding for the console (only if necessary)
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs  # Don't encode here
])

# Print the document text
try:
    print(docText.encode('utf-8'))  # Encode to handle printing special characters
except UnicodeEncodeError:
    print("Error encoding the text. There are characters that can't be displayed.")
