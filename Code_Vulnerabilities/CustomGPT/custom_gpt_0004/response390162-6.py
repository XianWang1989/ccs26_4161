
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define the grammar with nested structures and specific words
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                                 # Media chunk
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+|<VB.?(directed|acted)>} # Relation chunk with specific verbs
    ENTITY: {<NN.*>}                                          # Entity chunk
"""

def chunk_text(text):
    # Tokenize and POS tag the text
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    # Initialize the chunk parser
    chunk_parser = RegexpParser(grammar)

    # Chunk the tagged text
    chunked = chunk_parser.parse(tagged)
    return chunked

# Example phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
chunked_result = chunk_text(phrase)

# Print the result
print(chunked_result)
