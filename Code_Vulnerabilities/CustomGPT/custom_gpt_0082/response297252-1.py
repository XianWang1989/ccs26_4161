
import docx
import sys
import codecs

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Prepare the text with proper encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Decode the string to Unicode
docText = docText.decode('utf-8')

# Function to print Unicode safely
def safe_print(text):
    try:
        print(text.encode(sys.stdout.encoding, errors='replace'))
    except Exception as e:
        print("Error while printing:", e)

# Use the safe print function
safe_print(docText)
