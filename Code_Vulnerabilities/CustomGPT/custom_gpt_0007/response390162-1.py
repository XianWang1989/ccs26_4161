
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Media noun phrase
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}          # Relation phrase
    ENTITY: {<NN.*>}                             # Entity noun
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Sample sentence to parse
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Apply the chunk parser
chunked_sentence = chunk_parser.parse(tagged_tokens)

# Print the result
print(chunked_sentence)
