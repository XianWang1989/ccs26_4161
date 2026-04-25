
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs directly as Unicode
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text, ensuring it's properly handled as Unicode
print docText  # No need to decode since docText is already in Unicode
