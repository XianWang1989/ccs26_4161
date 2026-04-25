
import docx
import sys

# Set the default encoding to 'utf-8' for the terminal output in Python 2.7 
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])  # No need to encode here

# Print the text, it should handle special characters
print docText  # This will work now, assuming you've set up the default encoding
