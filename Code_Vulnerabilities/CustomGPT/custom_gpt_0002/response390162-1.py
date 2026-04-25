
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk sequences of DT, JJ, NN
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}      # Chunk verbs followed by media
    ENTITY: {<NN.*>}                          # Chunk singular/plural nouns
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)
chunks.draw()  # For visual representation (optional)
