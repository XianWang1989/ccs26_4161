
import docx

def read_docx(file_path):
    # Read the document
    document = docx.Document(file_path)

    # Collecting text from paragraphs without additional encoding
    docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

    # Print the document text
    print(docText)

# Example usage
read_docx('sim_dir_administrativo.docx')
