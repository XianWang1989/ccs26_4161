
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Create a list of paragraphs, ensuring each paragraph is handled as a Unicode string
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Output the text
# No need to decode since docText is already a Unicode string
print(docText)
