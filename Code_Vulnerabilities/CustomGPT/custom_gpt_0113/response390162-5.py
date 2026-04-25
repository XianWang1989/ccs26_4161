
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Assuming you have downloaded the necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*|directed|acted><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>+}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)
