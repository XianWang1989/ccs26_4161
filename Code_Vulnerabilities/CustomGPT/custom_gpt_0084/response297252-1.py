
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string, keeping them as unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text; ensure the terminal can handle UTF-8
try:
    print(docText.encode('utf-8'))
except UnicodeEncodeError:
    # If you encounter an encoding error, you can handle it gracefully
    print(docText.encode('utf-8', 'replace'))  # replace unencodable characters
