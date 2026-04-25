
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}               # Chunk sequences that represent media
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}       # Chunk sequences that indicate relation
  ENTITY: {<NN.*>}                         # Chunk entities (nouns)
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parsing the tagged tokens
result = chunk_parser.parse(tagged_tokens)

# Print the result
print(result)

# Optionally, you can visualize the chunked structure
result.draw()
