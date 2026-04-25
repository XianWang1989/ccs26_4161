
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
result = chunk_parser.parse(tagged_tokens)

# Print the chunked result
print(result)
