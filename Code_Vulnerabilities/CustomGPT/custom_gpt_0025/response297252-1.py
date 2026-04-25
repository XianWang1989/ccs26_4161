
import docx
import sys

# Set the default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text.encode('utf-8', 'ignore') for paragraph in document.paragraphs])

# Print the text
print docText.decode("utf-8")
