
import nltk
from nltk.chunk import RegexpParser
from nltk import pos_tag, word_tokenize

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk media types
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}      # Chunk relations
    ENTITY: {<NN.*>}                          # Chunk entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Perform the chunking
result = chunk_parser.parse(tagged)

# Draw the parse tree
result.draw()

# Print the result as a tree structure
print(result)
