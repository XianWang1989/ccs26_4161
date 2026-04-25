
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs' text safely
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# If you need to handle encoding for displaying in a terminal that may not support it
try:
    # Print the text directly without encoding
    print(docText)
except UnicodeEncodeError:
    # If there's an encoding error, encode to 'utf-8' and then decode it back
    print(docText.encode('utf-8').decode('utf-8'))
