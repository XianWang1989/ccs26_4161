
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}            # Chunk verb followed by NP (like 'featuring performances') 
    ENTITY: {<NN.*>}                              # Chunk any noun
"""

# Create a parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
parsed_tree = chunk_parser.parse(tagged)

# Display the chunked structure
print(parsed_tree)
parsed_tree.draw()  # Uncomment to view the chunk tree visually
