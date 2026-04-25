
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Create a unicode string from the paragraphs
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text, directly, since it's already in unicode
print docText  # This should work without explicit decoding in Python 2.7

# If you absolutely need to encode it somewhere else, do so like this:
encoded_text = docText.encode('utf-8')  # This is how to encode it if needed
