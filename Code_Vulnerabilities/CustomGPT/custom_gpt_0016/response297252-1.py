
import docx

# Load the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Create a string that joins all paragraphs
# Use 'unicode' instead of 'encode' to preserve characters
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Now print the unicode string. No need to decode, as it's already in unicode format
print docText
