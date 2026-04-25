
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                    # Media identification
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}            # Relation extraction
  ENTITY: {<NN.*>}                               # Entity identification
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
result = chunk_parser.parse(tagged)

# Display the results
print(result)

# Optionally, draw the tree structure
result.draw()
