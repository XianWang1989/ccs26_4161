
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs and ensure they are in Unicode
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text to the console, ensuring it handles special characters
try:
    print docText.encode('utf-8')  # Encode to utf-8 for output
except UnicodeEncodeError:
    print "Unable to encode some characters."

# Note: No need to decode docText, as it's already a Unicode string.
