
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the words
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}           # Media noun phrase
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}  # Relation verb phrase
    ENTITY: {<NN.*>}                     # Entity
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)
