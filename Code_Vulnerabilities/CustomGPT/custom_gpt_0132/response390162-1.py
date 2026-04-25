
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media noun phrases
  RELATION: {<V.*> <DT>?<JJ>*<NN.*>+}            # Relation phrases
  ENTITY: {<NN.*>}                               # Single entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the sentence
result = chunk_parser.parse(tagged_tokens)

# Display the results
print(result)

# Draw the chunk tree (requires GUI support)
result.draw()
